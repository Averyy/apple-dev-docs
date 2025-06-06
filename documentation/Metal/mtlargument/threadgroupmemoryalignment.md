# threadgroupMemoryAlignment

**Framework**: Metal  
**Kind**: property

The required byte alignment in memory for the threadgroup data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var threadgroupMemoryAlignment: Int { get }
```

#### Discussion

If the argument is not a threadgroup, querying this property is a fatal error. The Metal device determines this value.

## See Also

- [var threadgroupMemoryDataSize: Int](mtlargument/threadgroupmemorydatasize.md)
  The size, in bytes, of the threadgroup data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/threadgroupmemoryalignment)*