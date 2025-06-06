# warning(_:)

**Framework**: Swift  
**Kind**: macro

Produces the given warning message during compilation.

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
(declaration) macro warning(_ message: String)
```

#### Overview

Compilation proceeds after emitting the message as a nonfatal warning.

## Parameters

- `warning`: The diagnostic message.

## See Also

- [macro error(String)](error(_:).md)
  Emits the given message as a fatal error and terminates the compilation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/warning(_:))*