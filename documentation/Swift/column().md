# column()

**Framework**: Swift  
**Kind**: macro  
**Role**: Macro

Produces the column number in which the macro begins.

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
@freestanding(expression)
macro column<T>() -> T where T : ExpressibleByIntegerLiteral
```

## See Also

### Getting Source Location Information
- [macro file<T>() -> T](./file%28%29.md)
  Produces the path to the file in which it appears.
- [macro fileID<T>() -> T](./fileid%28%29.md)
  Produces a unique identifier for the source file in which the macro appears.
- [macro filePath<T>() -> T](./filepath%28%29.md)
  Produces the complete path to the file in which the macro appears.
- [macro function<T>() -> T](./function%28%29.md)
  Produces the name of the declaration in which it appears.
- [macro line<T>() -> T](./line%28%29.md)
  Produces the line number on which it appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/column())*