# PerformOperation

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
virtual kern_return_t PerformOperation(uint64_t options, uint64_t dmaOffset, uint64_t length, uint64_t dataOffset, IOMemoryDescriptor *data);
```

## See Also

### Performing Internal Operations
- [CompleteDMA](./completedma.md)
- [GetPreparation](./getpreparation.md)
- [PrepareForDMA](./preparefordma.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodmacommand/performoperation)*