# PerformOperation

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t PerformOperation(uint64_t options, uint64_t dmaOffset, uint64_t length, uint64_t dataOffset, IOMemoryDescriptor * data);
```

## See Also

- [CompleteDMA](iodmacommand/completedma.md)
- [GetPreparation](iodmacommand/getpreparation.md)
- [PrepareForDMA](iodmacommand/preparefordma.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodmacommand/performoperation)*