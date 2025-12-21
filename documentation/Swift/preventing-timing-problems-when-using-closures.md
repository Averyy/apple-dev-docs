# Preventing Timing Problems When Using Closures

**Framework**: Swift

Understand how different API calls to your closures can affect your app.

#### Overview

Many of the APIs you use in Swift take a closure—or a function passed as an instance—as a parameter. Because closures can contain code that interacts with multiple parts of an app, it’s important to understand the different ways closures can be called by the APIs you pass them to. Closures you pass to APIs can be called synchronously (immediately) or asynchronously (sometime later). They may be called once, many times, or never.

> ❗ **Important**: Making false assumptions about when a closure is called can lead to data inconsistency and app crashes.

##### Understand the Results of Synchronous and Asynchronous Calls

When you pass a closure to an API, consider  that closure will be called relative to the other code in your app. In synchronous APIs, the result of calling the closure will be available immediately after you pass the closure. In asynchronous APIs, the result won’t be available until sometime later; this difference affects how you write code both  your closure as well as the code  your closure.

The example below defines two functions, `now(_:)` and `later(_:)`. You can call both functions the same way: with a trailing closure and no other arguments. Both `now(_:)` and `later(_:)` accept a closure and call it, but `later(_:)` waits a couple seconds before calling its closure.

```swift
import Dispatch
let queue = DispatchQueue(label: "com.example.queue")

func now(_ closure: () -> Void) {
    closure()
}

func later(_ closure: @escaping () -> Void) {
    queue.asyncAfter(deadline: .now() + 2) {
        closure()
    }
}
```

The `now(_:)` and `later(_:)` functions represent the two most common categories of APIs you’ll encounter in methods from app frameworks that take closures: synchronous APIs like `now(_:)`, and asynchronous APIs like `later(_:)`.

Because calling a closure can change the local and global state of your app, the code you write on the lines after passing a closure needs to be written with a careful consideration of  that closure is called. Even something as simple as printing a sequence of letters can be affected by the timing of a closure call:

```swift
later {
    print("A") // Eventually prints "A"
}
print("B") // Immediately prints "B"

now {
    print("C") // Immediately prints "C"
}
print("D") // Immedately prints "D"

// Prevent the program from exiting immediately if you're running this code in Terminal.
let semaphore = DispatchSemaphore(value: 0).wait(timeout: .now() + 10)
```

Running the code in the example above usually prints the letters in the order `B` → `C` → `D` → `A`. Even though the line that prints `A` is first in the code, it’s ordered later in the output. The ordering difference happens due to the way the `now(_:)` and `later(_:)` functions are defined. You need to know how each function calls its closure if you write code that relies on a specific execution order.

> **Note**: The order in which `A` is printed relative to the other letters isn’t guaranteed. Under typical system conditions, it’s usually printed last, but you shouldn’t write code that relies on the order of an asychronous call relative to synchronous code without performing more careful synchronization between threads.

You’ll need to consider this kind of time-based execution problem frequently when using APIs that take closures. In many cases, only one sequence of calls is correct for your app, so it’s important to think through what the state of your app will be, given the APIs you’re using. Use API names and parameter names along with documentation to determine whether an API is synchronous or asynchronous.

A common timing mistake is expecting the results of an asynchronous call to be available within the calling synchronous code. For example, the `later(_:)` method above is comparable to the [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) class’s [`dataTask(with:completionHandler:)`](https://developer.apple.com/documentation/Foundation/URLSession/dataTask(with:completionHandler:)-52wk8) method, which is also asynchronous. A timing scenario you should avoid is calling the [`dataTask(with:completionHandler:)`](https://developer.apple.com/documentation/Foundation/URLSession/dataTask(with:completionHandler:)-52wk8) method within your app’s [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()) method and attempting to use the results outside of the closure you pass as the completion handler.

##### Dont Write Code That Makes a One Time Change in a Closure Thats Called Multiple Times

If you’re going to pass a closure to an API that might call it multiple times, omit code that’s intended to make a one-time change to external state.

The example below creates a [`FileHandle`](https://developer.apple.com/documentation/Foundation/FileHandle) and an array of data lines to write to the file that the handle refers to:

```swift
import Foundation

let file = FileHandle(forWritingAtPath: "/dev/null")!
let lines = ["x,y", "1,1", "2,4", "3,9", "4,16"]
```

To write each line to the file, pass a closure to the [`forEach(_:)`](array/foreach(_:).md) method:

```swift
lines.forEach { line in
    file.write("\(line)\n".data(using: .utf8)!)
}
```

When you’re finished using a [`FileHandle`](https://developer.apple.com/documentation/Foundation/FileHandle), close it using [`closeFile()`](https://developer.apple.com/documentation/Foundation/FileHandle/closeFile()). The correct placement of the call to [`closeFile()`](https://developer.apple.com/documentation/Foundation/FileHandle/closeFile()) is outside of the closure:

```swift
lines.forEach { line in
    file.write("\(line)\n".data(using: .utf8)!)
}

file.closeFile()
```

If you misunderstand the requirements of [`closeFile()`](https://developer.apple.com/documentation/Foundation/FileHandle/closeFile()), you might place the call inside the closure. Doing so crashes your app:

```swift
lines.forEach { line in
    file.write("\(line)\n".data(using: .utf8)!)
    file.closeFile() // Error
}
```

##### Dont Put Critical Code in a Closure That Might Not Be Called

If there’s a chance that a closure you pass to an API won’t be called, don’t put code that’s critical to continuing your app in the closure.

The example below defines a `Lottery` enumeration that randomly picks a winning number and calls a completion handler if the right number is guessed:

```swift
enum Lottery {
    static var lotteryWinHandler: (() -> Void)?

    @discardableResult static func pickWinner(guess: Int) {
        print("Running the lottery.")
        if guess == Int.random(in: 0 ..< 100_000_000), let winHandler = lotteryWinHandler {
            winHandler()
            return true
        }

        return false
    }
}
```

Writing code that depends on the completion handler being called is dangerous. There’s no guarantee that the random guess will be correct, so important actions like paying bills—scheduled for after you win the lottery—might never happen.

```swift
func payBills() {
    amountOwed = 0
}

var amountOwed = 25
let myLuckyNumber = 42

Lottery.lotteryWinHandler = {
    print("Congratulations!")
    payBills()
}

// You get 10 chances at winning.
for _ in 1...10 {
    Lottery.pickWinner(guess: myLuckyNumber)
}

if amountOwed > 0 {
    fatalError("You need to pay your bills before proceeding.")
}

// Code placed below this line runs only if the lottery was won.
```

## See Also

- [Maintaining State in Your Apps](maintaining-state-in-your-apps.md)
  Use enumerations to capture and track the state of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/preventing-timing-problems-when-using-closures)*