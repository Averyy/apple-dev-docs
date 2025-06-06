# PrepareForDMA

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t PrepareForDMA(uint64_t options, IOMemoryDescriptor * memory, uint64_t offset, uint64_t length, uint64_t * flags, uint32_t * segmentsCount, IOAddressSegment segments[32]);
```

## See Also

- [CompleteDMA](iodmacommand/completedma.md)
- [GetPreparation](iodmacommand/getpreparation.md)
- [PerformOperation](iodmacommand/performoperation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodmacommand/preparefordma)*