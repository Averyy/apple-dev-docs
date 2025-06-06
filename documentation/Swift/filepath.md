# filePath()

**Framework**: Swift  
**Kind**: macro

Produces the complete path to the file in which the macro appears.

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
(expression) macro filePath<T>() -> T where T : ExpressibleByStringLiteral
```

#### Overview

Because `#fileID` doesn’t embed the full path to the source file, unlike `#filePath`, it gives you better privacy and reduces the size of the compiled binary. Avoid using `#filePath` outside of tests, build scripts, or other code that doesn’t become part of the shipping program.

This macro’s value can be changed by `#sourceLocation`, as described in [`Line Control Statement`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements#Line-Control-Statement) in .

## See Also

- [macro file<T>() -> T](file().md)
  Produces the path to the file in which it appears.
- [macro fileID<T>() -> T](fileid().md)
  Produces a unique identifier for the source file in which the macro appears.
- [macro function<T>() -> T](function().md)
  Produces the name of the declaration in which it appears.
- [macro line<T>() -> T](line().md)
  Produces the line number on which it appears.
- [macro column<T>() -> T](column().md)
  Produces the column number in which the macro begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/filepath())*