# append(_:count:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

### Adding Bytes
- [func append(Data)](./append%28_%29-vjwy.md)
  Appends the specified data to the end of this data.
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](./append%28_%29-xtlw.md)
  Append a buffer of bytes to the data.
- [func reserveCapacity(Int)](./reservecapacity%28_%29.md)
  Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/append(_:count:))*