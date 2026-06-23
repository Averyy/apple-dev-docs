# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the byte at the specified offset in the span.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
subscript(byteOffset: Int) -> UInt8 { get set }
```

## Parameters

- `byteOffset`: The offset of the byte to access. `byteOffset` must be greater than or equal to zero, and less than `byteCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/subscript(_:))*