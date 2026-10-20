# file()

**Framework**: Swift  
**Kind**: macro  
**Role**: Macro

Produces the path to the file in which it appears.

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
@freestanding
(expression) macro file<T>() -> T where T : ExpressibleByStringLiteral
```

#### Overview

The string value from `#file` depends on the language version, to enable migration from the old `#filePath` behavior to the new `#fileID` behavior. Currently, `#file` has the same value as `#filePath`. In a future version of Swift, `#file` will have the same value as `#fileID` instead. To adopt the future behavior, replace `#file` with `#fileID` or `#filePath` as appropriate.

This macro’s value can be changed by `#sourceLocation`, as described in [Line Control Statement](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements#Line-Control-Statement) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

## See Also

### Getting Source Location Information
- [macro fileID<T>() -> T](./fileid%28%29.md)
  Produces a unique identifier for the source file in which the macro appears.
- [macro filePath<T>() -> T](./filepath%28%29.md)
  Produces the complete path to the file in which the macro appears.
- [macro function<T>() -> T](./function%28%29.md)
  Produces the name of the declaration in which it appears.
- [macro line<T>() -> T](./line%28%29.md)
  Produces the line number on which it appears.
- [macro column<T>() -> T](./column%28%29.md)
  Produces the column number in which the macro begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/file())*