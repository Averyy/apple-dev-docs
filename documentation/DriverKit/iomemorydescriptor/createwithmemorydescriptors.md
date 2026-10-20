# CreateWithMemoryDescriptors

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit 20.0+
- iOS
- iPadOS
- macOS

## Declaration

```c
static kern_return_t CreateWithMemoryDescriptors(uint64_t memoryDescriptorCreateOptions, uint32_t withDescriptorsCount, IOMemoryDescriptor * const withDescriptors[32], IOMemoryDescriptor **memory);
```

## See Also

### Type Methods
- [CreateSubMemoryDescriptor](./createsubmemorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/createwithmemorydescriptors)*