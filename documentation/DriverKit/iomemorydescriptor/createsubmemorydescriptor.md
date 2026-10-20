# CreateSubMemoryDescriptor

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
static kern_return_t CreateSubMemoryDescriptor(uint64_t memoryDescriptorCreateOptions, uint64_t offset, uint64_t length, IOMemoryDescriptor *ofDescriptor, IOMemoryDescriptor **memory);
```

## See Also

### Type Methods
- [CreateWithMemoryDescriptors](./createwithmemorydescriptors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/createsubmemorydescriptor)*