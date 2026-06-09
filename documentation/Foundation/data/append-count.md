# append(_:count:)

**Framework**: Foundation  
**Kind**: method

Appends the specified bytes from memory to the end of the data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func append(_ bytes: UnsafePointer<UInt8>, count: Int)
```

## See Also

- [func append(Data)](data/append(_:)-vjwy.md)
  Appends the specified data to the end of this data.
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](data/append(_:)-xtlw.md)
  Append a buffer of bytes to the data.
- [func reserveCapacity(Int)](data/reservecapacity(_:).md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/append(_:count:))*