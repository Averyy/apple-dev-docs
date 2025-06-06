# withoutActuallyEscaping(_:do:)

**Framework**: Swift  
**Kind**: func

Allows a nonescaping closure to temporarily be used as if it were allowed to escape.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func withoutActuallyEscaping<ClosureType, ResultType, Failure>(_ closure: ClosureType, do body: (ClosureType) throws(Failure) -> ResultType) throws(Failure) -> ResultType where Failure : Error
```

#### Return Value

The return value, if any, of the `body` closure.

#### Discussion

You can use this function to call an API that takes an escaping closure in a way that doesn’t allow the closure to escape in practice. The examples below demonstrate how to use `withoutActuallyEscaping(_:do:)` in conjunction with two common APIs that use escaping closures: lazy collection views and asynchronous operations.

The following code declares an `allValues(in:match:)` function that checks whether all the elements in an array match a predicate. The function won’t compile as written, because a lazy collection’s `filter(_:)` method requires an escaping closure. The lazy collection isn’t persisted, so the `predicate` closure won’t actually escape the body of the function; nevertheless, it can’t be used in this way.

```swift
func allValues(in array: [Int], match predicate: (Int) -> Bool) -> Bool {
    return array.lazy.filter { !predicate($0) }.isEmpty
}
// error: closure use of non-escaping parameter 'predicate'...
```

`withoutActuallyEscaping(_:do:)` provides a temporarily escapable copy of `predicate` that  be used in a call to the lazy view’s `filter(_:)` method. The second version of `allValues(in:match:)` compiles without error, with the compiler guaranteeing that the `escapablePredicate` closure doesn’t last beyond the call to `withoutActuallyEscaping(_:do:)`.

```swift
func allValues(in array: [Int], match predicate: (Int) -> Bool) -> Bool {
    return withoutActuallyEscaping(predicate) { escapablePredicate in
        array.lazy.filter { !escapablePredicate($0) }.isEmpty
    }
}
```

Asynchronous calls are another type of API that typically escape their closure arguments. The following code declares a `perform(_:simultaneouslyWith:)` function that uses a dispatch queue to execute two closures concurrently.

```swift
func perform(_ f: () -> Void, simultaneouslyWith g: () -> Void) {
    let queue = DispatchQueue(label: "perform", attributes: .concurrent)
    queue.async(execute: f)
    queue.async(execute: g)
    queue.sync(flags: .barrier) {}
}
// error: passing non-escaping parameter 'f'...
// error: passing non-escaping parameter 'g'...
```

The `perform(_:simultaneouslyWith:)` function ends with a call to the `sync(flags:execute:)` method using the `.barrier` flag, which forces the function to wait until both closures have completed running before returning. Even though the barrier guarantees that neither closure will escape the function, the `async(execute:)` method still requires that the closures passed be marked as `@escaping`, so the first version of the function does not compile. To resolve these errors, you can use `withoutActuallyEscaping(_:do:)` to get copies of `f` and `g` that can be passed to `async(execute:)`.

```swift
func perform(_ f: () -> Void, simultaneouslyWith g: () -> Void) {
    withoutActuallyEscaping(f) { escapableF in
        withoutActuallyEscaping(g) { escapableG in
            let queue = DispatchQueue(label: "perform", attributes: .concurrent)
            queue.async(execute: escapableF)
            queue.async(execute: escapableG)
            queue.sync(flags: .barrier) {}
        }
    }
}
```

> ❗ **Important**: The escapable copy of `closure` passed to `body` is only valid during the call to `withoutActuallyEscaping(_:do:)`. It is undefined behavior for the escapable closure to be stored, referenced, or executed after the function returns.

The escapable copy of `closure` passed to `body` is only valid during the call to `withoutActuallyEscaping(_:do:)`. It is undefined behavior for the escapable closure to be stored, referenced, or executed after the function returns.

## Parameters

- `closure`: A nonescaping closure value that is made escapable for the   duration of the execution of the   closure. If   has a   return value, that value is also used as the return value for the    function.
- `body`: A closure that is executed immediately with an escapable copy of    as its argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withoutactuallyescaping(_:do:))*