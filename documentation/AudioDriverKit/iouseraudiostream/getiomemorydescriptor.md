# GetIOMemoryDescriptor

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the memory descriptor the stream uses for I/O.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
OSSharedPtr<IOMemoryDescriptor> GetIOMemoryDescriptor();
```

## Discussion

This is the value provided to the stream’s initializer, or updated later by a call to [`SetIOMemoryDescriptor`](./setiomemorydescriptor.md).

## See Also

### Working with Memory Descriptors
- [SetIOMemoryDescriptor](./setiomemorydescriptor.md)
  Sets the memory descriptor the stream uses for I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/getiomemorydescriptor)*