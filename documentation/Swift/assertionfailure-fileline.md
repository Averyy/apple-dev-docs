# assertionFailure(_:file:line:)

**Framework**: Swift  
**Kind**: func

Indicates that an internal consistency check failed.

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
func assertionFailure(_ message: @autoclosure () -> String = String(), file: StaticString = #file, line: UInt = #line)
```

#### Discussion

This function’s effect varies depending on the build flag used:

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration), stop program execution in a debuggable state after printing `message`.
- In `-O` builds, has no effect.
- In `-Ounchecked` builds, the optimizer may assume that this function is never called. Failure to satisfy that assumption is a serious programming error.

## Parameters

- `message`: A string to print in a playground or   build. The   default is an empty string.
- `file`: The file name to print with  . The default is the file   where   is called.
- `line`: The line number to print along with  . The default is the   line number where   is called.

## See Also

- [func assert(@autoclosure () -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](assert(_:_:file:line:).md)
  Performs a traditional C-style assert with an optional message.
- [func precondition(@autoclosure () -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](precondition(_:_:file:line:).md)
  Checks a necessary condition for making forward progress.
- [func preconditionFailure(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](preconditionfailure(_:file:line:).md)
  Indicates that a precondition was violated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/assertionfailure(_:file:line:))*