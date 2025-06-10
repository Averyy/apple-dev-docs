# CommandLine

**Framework**: Swift  
**Kind**: enum

Command-line arguments for the current process.

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
@frozen
enum CommandLine
```

## Topics

### Accessing Arguments
- [static var arguments: [String]](commandline/arguments.md)
  An array that provides access to this program’s command line arguments.
### Accessing Raw Argument Data
- [static var argc: Int32](commandline/argc.md)
  Access to the raw argc value from C.
- [static var unsafeArgv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>](commandline/unsafeargv.md)
  Access to the raw argv value from C.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [func readLine(strippingNewline: Bool) -> String?](readline(strippingnewline:).md)
  Returns a string read from standard input through the end of the current line or until EOF is reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/commandline)*