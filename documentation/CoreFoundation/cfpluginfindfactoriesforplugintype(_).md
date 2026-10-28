# CFPlugInFindFactoriesForPlugInType(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Searches all registered plug-ins for factory functions capable of creating an instance of the given type.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFPlugInFindFactoriesForPlugInType(_ typeUUID: CFUUID!) -> CFArray!
```

```c
extern CFArrayRefCFPlugInFindFactoriesForPlugInType(CFUUIDRef typeUUID);
```

## Return Value

An array of UUIDs for factory functions capable of creating an instance of the given type.

## Parameters

- `typeUUID`: A UUID type.

## See Also

### CFPlugIn Miscellaneous Functions
- [func CFPlugInAddInstanceForFactory(CFUUID!)](./cfpluginaddinstanceforfactory%28_%29.md)
  Registers a new instance of a type with `CFPlugIn`.
- [func CFPlugInFindFactoriesForPlugInTypeInPlugIn(CFUUID!, CFPlugIn!) -> CFArray!](./cfpluginfindfactoriesforplugintypeinplugin%28_,_%29.md)
  Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [func CFPlugInGetBundle(CFPlugIn!) -> CFBundle!](./cfplugingetbundle%28_%29.md)
  Returns a plug-in’s bundle.
- [func CFPlugInGetTypeID() -> CFTypeID](./cfplugingettypeid%28%29.md)
  Returns the type identifier for the `CFPlugIn` opaque type.
- [func CFPlugInIsLoadOnDemand(CFPlugIn!) -> Bool](./cfpluginisloadondemand%28_%29.md)
  Determines whether or not a plug-in is loaded on demand.
- [func CFPlugInRemoveInstanceForFactory(CFUUID!)](./cfpluginremoveinstanceforfactory%28_%29.md)
  Unregisters an instance of a type with `CFPlugIn`.
- [func CFPlugInSetLoadOnDemand(CFPlugIn!, Bool)](./cfpluginsetloadondemand%28_,_%29.md)
  Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginfindfactoriesforplugintype(_:))*