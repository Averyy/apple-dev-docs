# reserveCapacity(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.

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
mutating func reserveCapacity(_ minimumCapacity: Int)
```

## Discussion

If you will be adding a known number of elements to a collection, use this method to avoid multiple reallocations. A type that conforms to `RangeReplaceableCollection` can choose how to respond when this method is called. Depending on the type, it may make sense to allocate more or less storage than requested or to take no action at all.

## Parameters

- `minimumCapacity`: The requested number of elements to store.

## See Also

### Adding Bytes
- [func append(Data)](./append%28_%29-vjwy.md)
  Appends the specified data to the end of this data.
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](./append%28_%29-xtlw.md)
  Append a buffer of bytes to the data.
- [func append(UnsafePointer<UInt8>, count: Int)](./append%28_,count%29.md)
  Appends the specified bytes from memory to the end of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/reservecapacity(_:))*