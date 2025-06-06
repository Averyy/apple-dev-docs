# CreateSubMemoryDescriptor

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit 20.0+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static kern_return_t CreateSubMemoryDescriptor(uint64_t memoryDescriptorCreateOptions, uint64_t offset, uint64_t length, IOMemoryDescriptor * ofDescriptor, IOMemoryDescriptor * * memory);
```

## See Also

- [CreateWithMemoryDescriptors](iomemorydescriptor/createwithmemorydescriptors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iomemorydescriptor/createsubmemorydescriptor)*