# CFPlugInIsLoadOnDemand(_:)

**Framework**: Core Foundation  
**Kind**: func

Determines whether or not a plug-in is loaded on demand.

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
func CFPlugInIsLoadOnDemand(_ plugIn: CFPlugIn!) -> Bool
```

#### Return Value

`true` if the plug-in is loaded only when a client requests an instance of a supported type, otherwise  `false`.

#### Discussion

Plug-ins that do static registration are load on demand by default. Plug-ins that do dynamic registration are not load on demand by default.

## Parameters

- `plugIn`: The plug-in to query.

## See Also

- [func CFPlugInAddInstanceForFactory(CFUUID!)](cfpluginaddinstanceforfactory(_:).md)
  Registers a new instance of a type with `CFPlugIn`.
- [func CFPlugInFindFactoriesForPlugInType(CFUUID!) -> CFArray!](cfpluginfindfactoriesforplugintype(_:).md)
  Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [func CFPlugInFindFactoriesForPlugInTypeInPlugIn(CFUUID!, CFPlugIn!) -> CFArray!](cfpluginfindfactoriesforplugintypeinplugin(_:_:).md)
  Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [func CFPlugInGetBundle(CFPlugIn!) -> CFBundle!](cfplugingetbundle(_:).md)
  Returns a plug-in’s bundle.
- [func CFPlugInGetTypeID() -> CFTypeID](cfplugingettypeid().md)
  Returns the type identifier for the `CFPlugIn` opaque type.
- [func CFPlugInRemoveInstanceForFactory(CFUUID!)](cfpluginremoveinstanceforfactory(_:).md)
  Unregisters an instance of a type with `CFPlugIn`.
- [func CFPlugInSetLoadOnDemand(CFPlugIn!, Bool)](cfpluginsetloadondemand(_:_:).md)
  Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginisloadondemand(_:))*