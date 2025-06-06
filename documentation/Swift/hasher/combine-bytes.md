# combine(bytes:)

**Framework**: Swift  
**Kind**: method

Adds the contents of the given buffer to this hasher, mixing it into the hasher state.

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
mutating func combine(bytes: UnsafeRawBufferPointer)
```

## Parameters

- `bytes`: A raw memory buffer.

## See Also

- [func combine<H>(H)](hasher/combine(_:).md)
  Adds the given value to this hasher, mixing its essential parts into the hasher state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/hasher/combine(bytes:))*