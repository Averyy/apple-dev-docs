# PrepareForDMA

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t PrepareForDMA(uint64_t options, IOMemoryDescriptor *memory, uint64_t offset, uint64_t length, uint64_t *flags, uint32_t *segmentsCount, IOAddressSegment segments[32]);
```

## See Also

### Performing Internal Operations
- [CompleteDMA](./completedma.md)
- [GetPreparation](./getpreparation.md)
- [PerformOperation](./performoperation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodmacommand/preparefordma)*