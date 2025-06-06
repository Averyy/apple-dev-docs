# combine(_:)

**Framework**: Swift  
**Kind**: method

Adds the given value to this hasher, mixing its essential parts into the hasher state.

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
mutating func combine<H>(_ value: H) where H : Hashable
```

## Parameters

- `value`: A value to add to the hasher.

## See Also

- [func combine(bytes: UnsafeRawBufferPointer)](hasher/combine(bytes:).md)
  Adds the contents of the given buffer to this hasher, mixing it into the hasher state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/hasher/combine(_:))*