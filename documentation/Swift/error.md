# error(_:)

**Framework**: Swift  
**Kind**: macro

Emits the given message as a fatal error and terminates the compilation process.

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
(declaration) macro error(_ message: String)
```

## Parameters

- `message`: The error message.

## See Also

- [macro warning(String)](warning(_:).md)
  Produces the given warning message during compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/error(_:))*