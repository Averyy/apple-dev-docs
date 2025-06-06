# precondition(_:_:file:line:)

**Framework**: Swift  
**Kind**: func

Checks a necessary condition for making forward progress.

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
func precondition(_ condition: @autoclosure () -> Bool, _ message: @autoclosure () -> String = String(), file: StaticString = #file, line: UInt = #line)
```

#### Discussion

Use this function to detect conditions that must prevent the program from proceeding, even in shipping code.

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration): If `condition` evaluates to `false`, stop program execution in a debuggable state after printing `message`.
- In `-O` builds (the default for Xcode’s Release configuration): If `condition` evaluates to `false`, stop program execution.
- In `-Ounchecked` builds, `condition` is not evaluated, but the optimizer may assume that it  evaluates to `true`. Failure to satisfy that assumption is a serious programming error.

## Parameters

- `condition`: The condition to test.   is not evaluated in    builds.
- `message`: A string to print if   is evaluated to   in a   playground or   build. The default is an empty string.
- `file`: The file name to print with   if the precondition fails.   The default is the file where   is   called.
- `line`: The line number to print along with   if the assertion   fails. The default is the line number where    is called.

## See Also

- [func assert(@autoclosure () -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](assert(_:_:file:line:).md)
  Performs a traditional C-style assert with an optional message.
- [func assertionFailure(@autoclosure () -> String, file: StaticString, line: UInt)](assertionfailure(_:file:line:).md)
  Indicates that an internal consistency check failed.
- [func preconditionFailure(@autoclosure () -> String, file: StaticString, line: UInt) -> Never](preconditionfailure(_:file:line:).md)
  Indicates that a precondition was violated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/precondition(_:_:file:line:))*