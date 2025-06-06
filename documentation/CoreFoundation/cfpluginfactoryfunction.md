# CFPlugInFactoryFunction

**Framework**: Core Foundation  
**Kind**: typealias

Callback function that a plug-in author must implement to create a plug-in instance.

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
typealias CFPlugInFactoryFunction = (CFAllocator?, CFUUID?) -> UnsafeMutableRawPointer?
```

#### Discussion

The plug-in author’s implementation of this function is registered with `CFPlugIn` either statically in the plug-in’s information property list, or dynamically. This function is executed as a result of a call to [`CFPlugInInstanceCreate(_:_:_:)`](cfplugininstancecreate(_:_:_:).md) by the plug-in host.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the default allocator.
- `typeUUID`: The UUID type to instantiate.

## See Also

- [typealias CFPlugInDynamicRegisterFunction](cfplugindynamicregisterfunction.md)
  A callback which provides a plug-in the opportunity to dynamically register its types with a host.
- [typealias CFPlugInUnloadFunction](cfpluginunloadfunction.md)
  Callback function that is called, if present, just before a plug-in’s code is unloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginfactoryfunction)*