# CFPlugInGetBundle(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a plug-in’s bundle.

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
func CFPlugInGetBundle(_ plugIn: CFPlugIn!) -> CFBundle!
```

#### Return Value

The bundle for `plugIn`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

You should  use this function to get a plug-in’s bundle. Never attempt to access the plug-in directly as a bundle.

## Parameters

- `plugIn`: The plug-in whose bundle to obtain.

## See Also

- [func CFPlugInAddInstanceForFactory(CFUUID!)](cfpluginaddinstanceforfactory(_:).md)
  Registers a new instance of a type with `CFPlugIn`.
- [func CFPlugInFindFactoriesForPlugInType(CFUUID!) -> CFArray!](cfpluginfindfactoriesforplugintype(_:).md)
  Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [func CFPlugInFindFactoriesForPlugInTypeInPlugIn(CFUUID!, CFPlugIn!) -> CFArray!](cfpluginfindfactoriesforplugintypeinplugin(_:_:).md)
  Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [func CFPlugInGetTypeID() -> CFTypeID](cfplugingettypeid().md)
  Returns the type identifier for the `CFPlugIn` opaque type.
- [func CFPlugInIsLoadOnDemand(CFPlugIn!) -> Bool](cfpluginisloadondemand(_:).md)
  Determines whether or not a plug-in is loaded on demand.
- [func CFPlugInRemoveInstanceForFactory(CFUUID!)](cfpluginremoveinstanceforfactory(_:).md)
  Unregisters an instance of a type with `CFPlugIn`.
- [func CFPlugInSetLoadOnDemand(CFPlugIn!, Bool)](cfpluginsetloadondemand(_:_:).md)
  Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugingetbundle(_:))*