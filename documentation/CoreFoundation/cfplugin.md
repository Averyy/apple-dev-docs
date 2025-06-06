# CFPlugIn

**Framework**: Core Foundation  
**Kind**: class

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
class CFPlugIn
```

#### Overview

`CFPlugIn` provides a standard architecture for application extensions. With `CFPlugIn`, you can design your application as a host framework that uses a set of executable code modules called plug-ins to provide certain well-defined areas of functionality. This approach allows third-party developers to add features to your application without requiring access to your source code. You can also bundle together plug-ins for multiple platforms and let `CFPlugIn` transparently load the appropriate plug-in at runtime. You can use `CFPlugIn` to add plug-in capability to, or write a plug-in for, your application.

## Topics

### Creating Plug-ins
- [func CFPlugInCreate(CFAllocator!, CFURL!) -> CFPlugIn!](cfplugincreate(_:_:).md)
  Creates a CFPlugIn given its URL.
- [func CFPlugInInstanceCreate(CFAllocator!, CFUUID!, CFUUID!) -> UnsafeMutableRawPointer!](cfplugininstancecreate(_:_:_:).md)
  Creates a `CFPlugIn` instance of a given type using a given factory.
### Registration
- [func CFPlugInRegisterFactoryFunction(CFUUID!, CFPlugInFactoryFunction!) -> Bool](cfpluginregisterfactoryfunction(_:_:).md)
  Registers a factory function and its UUID with a `CFPlugIn` object.
- [func CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Bool](cfpluginregisterfactoryfunctionbyname(_:_:_:).md)
  Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [func CFPlugInRegisterPlugInType(CFUUID!, CFUUID!) -> Bool](cfpluginregisterplugintype(_:_:).md)
  Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](cfpluginunregisterfactory(_:).md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](cfpluginunregisterplugintype(_:_:).md)
  Removes the given type from a plug-in’s list of registered types.
### CFPlugIn Miscellaneous Functions
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
- [func CFPlugInIsLoadOnDemand(CFPlugIn!) -> Bool](cfpluginisloadondemand(_:).md)
  Determines whether or not a plug-in is loaded on demand.
- [func CFPlugInRemoveInstanceForFactory(CFUUID!)](cfpluginremoveinstanceforfactory(_:).md)
  Unregisters an instance of a type with `CFPlugIn`.
- [func CFPlugInSetLoadOnDemand(CFPlugIn!, Bool)](cfpluginsetloadondemand(_:_:).md)
  Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).
### Callbacks
- [typealias CFPlugInDynamicRegisterFunction](cfplugindynamicregisterfunction.md)
  A callback which provides a plug-in the opportunity to dynamically register its types with a host.
- [typealias CFPlugInFactoryFunction](cfpluginfactoryfunction.md)
  Callback function that a plug-in author must implement to create a plug-in instance.
- [typealias CFPlugInUnloadFunction](cfpluginunloadfunction.md)
  Callback function that is called, if present, just before a plug-in’s code is unloaded.
### Constants
- [Information Property List Keys](cfplugin-information-property-list-keys.md)
  A plug-in’s information property list can contain these keys used for registering types, factories, and interfaces.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugin)*