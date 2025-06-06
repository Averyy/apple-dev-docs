# assert(_:_:file:line:)

**Framework**: Swift  
**Kind**: func

Performs a traditional C-style assert with an optional message.

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
func assert(_ condition: @autoclosure () -> Bool, _ message: @autoclosure () -> String = String(), file: StaticString = #file, line: UInt = #line)
```

#### Discussion

Use this function for internal consistency checks that are active during testing but do not impact performance of shipping code. To check for invalid usage in Release builds, see `precondition(_:_:file:line:)`.

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration): If `condition` evaluates to `false`, stop program execution in a debuggable state after printing `message`.
- In `-O` builds (the default for Xcode’s Release configuration), `condition` is not evaluated, and there are no effects.
- In `-Ounchecked` builds, `condition` is not evaluated, but the optimizer may assume that it  evaluates to `true`. Failure to satisfy that assumption is a serious programming error.

## Parameters

- `condition`: The condition to test.   is only evaluated in   playgrounds and   builds.
- `message`: A string to print if   is evaluated to  . The   default is an empty string.
- `file`: The file name to print with   if the assertion fails. The   default is the file where   is called.
- `line`: The line number to print along with   if the assertion   fails. The default is the line number where    is called.

## See Also

- [func assertionFailure(@autoclosure () -> String, file: StaticString, line: UInt)](assertionfailure(_:file:line:).md)
  Indicates that an internal consistency check failed.
- [func precondition(@autoclosure () -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](precondition(_:_:file:line:).md)
  Checks a necessary condition for making forward progress.
- [func preconditionFailure(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](preconditionfailure(_:file:line:).md)
  Indicates that a precondition was violated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/assert(_:_:file:line:))*