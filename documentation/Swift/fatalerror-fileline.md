# fatalError(_:file:line:)

**Framework**: Swift  
**Kind**: func

Unconditionally prints a given message and stops execution.

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
func fatalError(_ message: @autoclosure () -> String = String(), file: StaticString = #file, line: UInt = #line) -> Never
```

## Parameters

- `message`: The string to print. The default is an empty string.
- `file`: The file name to print with  . The default is the file   where   is called.
- `line`: The line number to print along with  . The default is the   line number where   is called.

## See Also

- [enum Never](never.md)
  A type that has no values and can’t be constructed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/fatalerror(_:file:line:))*