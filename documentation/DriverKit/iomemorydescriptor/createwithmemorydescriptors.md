# CreateWithMemoryDescriptors

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit 20.0+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static kern_return_t CreateWithMemoryDescriptors(uint64_t memoryDescriptorCreateOptions, uint32_t withDescriptorsCount, IOMemoryDescriptor * const withDescriptors[32], IOMemoryDescriptor * * memory);
```

## See Also

- [CreateSubMemoryDescriptor](iomemorydescriptor/createsubmemorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/createwithmemorydescriptors)*