# threadgroupMemoryDataSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The size, in bytes, of the threadgroup data.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var threadgroupMemoryDataSize: Int { get }
```

```objc
@property (readonly) NSUInteger threadgroupMemoryDataSize;
```

## Discussion

If the argument is not a threadgroup, querying this property is a fatal error. The Metal device determines this value.

## See Also

### Describing a threadgroup memory argument
- [var threadgroupMemoryAlignment: Int](./threadgroupmemoryalignment.md)
  The required byte alignment in memory for the threadgroup data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/threadgroupmemorydatasize)*