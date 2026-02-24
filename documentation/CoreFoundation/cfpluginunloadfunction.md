# CFPlugInUnloadFunction

**Framework**: Core Foundation  
**Kind**: typealias

Callback function that is called, if present, just before a plug-in’s code is unloaded.

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
typealias CFPlugInUnloadFunction = (CFPlugIn?) -> Void
```

## Parameters

- `plugIn`: The `CFPlugIn` object that is about to be unloaded from memory. When writing in C++, this parameter functions as a `this` pointer for the plug-in.

## See Also

- [typealias CFPlugInDynamicRegisterFunction](cfplugindynamicregisterfunction.md)
  A callback which provides a plug-in the opportunity to dynamically register its types with a host.
- [typealias CFPlugInFactoryFunction](cfpluginfactoryfunction.md)
  Callback function that a plug-in author must implement to create a plug-in instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginunloadfunction)*