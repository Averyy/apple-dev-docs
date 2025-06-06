# GetIOMemoryDescriptor

**Framework**: AudioDriverKit  
**Kind**: method

Gets the memory descriptor the stream uses for I/O.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
OSSharedPtr<IOMemoryDescriptor> GetIOMemoryDescriptor();
```

#### Discussion

This is the value provided to the stream’s initializer, or updated later by a call to [`SetIOMemoryDescriptor`](iouseraudiostream/setiomemorydescriptor.md).

## See Also

- [SetIOMemoryDescriptor](iouseraudiostream/setiomemorydescriptor.md)
  Sets the memory descriptor the stream uses for I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/getiomemorydescriptor)*