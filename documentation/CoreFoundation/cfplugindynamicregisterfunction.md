# CFPlugInDynamicRegisterFunction

**Framework**: Core Foundation  
**Kind**: typealias

A callback which provides a plug-in the opportunity to dynamically register its types with a host.

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
typealias CFPlugInDynamicRegisterFunction = (CFPlugIn?) -> Void
```

#### Discussion

This callback is called as a plug-in is being loaded. This provides the plugin the means to dynamically register its types and factories with a plug-in’s host. The call is triggered by the presence of [`kCFPlugInDynamicRegistrationKey`](kcfplugindynamicregistrationkey.md) in the plug-in’s information property list.

## Parameters

- `plugIn`: The   object that is engaged in dynamic registration. When using in C++, this parameter functions as a   pointer for the plug-in.

## See Also

- [typealias CFPlugInFactoryFunction](cfpluginfactoryfunction.md)
  Callback function that a plug-in author must implement to create a plug-in instance.
- [typealias CFPlugInUnloadFunction](cfpluginunloadfunction.md)
  Callback function that is called, if present, just before a plug-in’s code is unloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugindynamicregisterfunction)*