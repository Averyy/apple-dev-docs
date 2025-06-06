# arguments

**Framework**: Swift  
**Kind**: property

An array that provides access to this program’s command line arguments.

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
static var arguments: [String] { get set }
```

#### Discussion

Use `CommandLine.arguments` to access the command line arguments used when executing the current program. The name of the executed program is the first argument.

The following example shows a command line executable that squares the integer given as an argument.

```swift
if CommandLine.arguments.count == 2,
   let number = Int(CommandLine.arguments[1]) {
    print("\(number) x \(number) is \(number * number)")
} else {
    print(
      """
      Error: Please provide a number to square.
      Usage: command <number>
      """
    )
}
```

Running the program results in the following output:

```swift
$ command 5
5 x 5 is 25
$ command ZZZ
Error: Please provide a number to square.
Usage: command <number>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/commandline/arguments)*