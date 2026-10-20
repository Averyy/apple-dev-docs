# CreateMemoryDescriptorFromClient

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 20.0+
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t CreateMemoryDescriptorFromClient(uint64_t memoryDescriptorCreateOptions, uint32_t segmentsCount, const IOAddressSegment segments[32], IOMemoryDescriptor **memory);
```

## See Also

### Instance Methods
- [CopyClientEntitlements](./copycliententitlements.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclient/creatememorydescriptorfromclient)*