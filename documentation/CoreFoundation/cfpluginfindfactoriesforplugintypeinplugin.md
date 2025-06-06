# CFPlugInFindFactoriesForPlugInTypeInPlugIn(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Searches the given plug-in for factory functions capable of creating an instance of the given type.

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
func CFPlugInFindFactoriesForPlugInTypeInPlugIn(_ typeUUID: CFUUID!, _ plugIn: CFPlugIn!) -> CFArray!
```

#### Return Value

An array of UUIDs for factory functions capable of creating an instance of the given type.

## Parameters

- `typeUUID`: A UUID type.
- `plugIn`: The plug-in to search.

## See Also

- [func CFPlugInAddInstanceForFactory(CFUUID!)](cfpluginaddinstanceforfactory(_:).md)
  Registers a new instance of a type with `CFPlugIn`.
- [func CFPlugInFindFactoriesForPlugInType(CFUUID!) -> CFArray!](cfpluginfindfactoriesforplugintype(_:).md)
  Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [func CFPlugInGetBundle(CFPlugIn!) -> CFBundle!](cfplugingetbundle(_:).md)
  Returns a plug-in’s bundle.
- [func CFPlugInGetTypeID() -> CFTypeID](cfplugingettypeid().md)
  Returns the type identifier for the `CFPlugIn` opaque type.
- [func CFPlugInIsLoadOnDemand(CFPlugIn!) -> Bool](cfpluginisloadondemand(_:).md)
  Determines whether or not a plug-in is loaded on demand.
- [func CFPlugInRemoveInstanceForFactory(CFUUID!)](cfpluginremoveinstanceforfactory(_:).md)
  Unregisters an instance of a type with `CFPlugIn`.
- [func CFPlugInSetLoadOnDemand(CFPlugIn!, Bool)](cfpluginsetloadondemand(_:_:).md)
  Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginfindfactoriesforplugintypeinplugin(_:_:))*