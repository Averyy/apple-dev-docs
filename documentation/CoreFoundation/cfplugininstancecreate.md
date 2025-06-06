# CFPlugInInstanceCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a `CFPlugIn` instance of a given type using a given factory.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFPlugInInstanceCreate(_ allocator: CFAllocator!, _ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> UnsafeMutableRawPointer!
```

#### Return Value

Returns the IUnknown interface for the new plug-in.

#### Discussion

The plug-in host uses this function to create an instance of the given type. Unless the plug-in is using dynamic registration, this function causes the plug-in’s code to be loaded into memory.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the default allocator.
- `factoryUUID`: The UUID representing the factory function to use to create a plug-in of the given type.
- `typeUUID`: The UUID type.

## See Also

- [func CFPlugInCreate(CFAllocator!, CFURL!) -> CFPlugIn!](cfplugincreate(_:_:).md)
  Creates a CFPlugIn given its URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugininstancecreate(_:_:_:))*