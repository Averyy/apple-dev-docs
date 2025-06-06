# CreateMemoryDescriptorFromClient

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit 20.0+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t CreateMemoryDescriptorFromClient(uint64_t memoryDescriptorCreateOptions, uint32_t segmentsCount, const IOAddressSegment segments[32], IOMemoryDescriptor * * memory);
```

## See Also

- [CopyClientEntitlements](iouserclient/copycliententitlements.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iouserclient/creatememorydescriptorfromclient)*