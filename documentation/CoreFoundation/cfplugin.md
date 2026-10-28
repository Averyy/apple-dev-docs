# CFPlugIn

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

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
class CFPlugIn
```

```c
typedef struct __CFBundle * CFPlugInRef;
```

## Overview

`CFPlugIn` provides a standard architecture for application extensions. With `CFPlugIn`, you can design your application as a host framework that uses a set of executable code modules called plug-ins to provide certain well-defined areas of functionality. This approach allows third-party developers to add features to your application without requiring access to your source code. You can also bundle together plug-ins for multiple platforms and let `CFPlugIn` transparently load the appropriate plug-in at runtime. You can use `CFPlugIn` to add plug-in capability to, or write a plug-in for, your application.

## Topics

### Creating Plug-ins
- [func CFPlugInCreate(CFAllocator!, CFURL!) -> CFPlugIn!](./cfplugincreate%28_,_%29.md)
  Creates a CFPlugIn given its URL.
- [func CFPlugInInstanceCreate(CFAllocator!, CFUUID!, CFUUID!) -> UnsafeMutableRawPointer!](./cfplugininstancecreate%28_,_,_%29.md)
  Creates a `CFPlugIn` instance of a given type using a given factory.
### Registration
- [func CFPlugInRegisterFactoryFunction(CFUUID!, CFPlugInFactoryFunction!) -> Bool](./cfpluginregisterfactoryfunction%28_,_%29.md)
  Registers a factory function and its UUID with a `CFPlugIn` object.
- [func CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Bool](./cfpluginregisterfactoryfunctionbyname%28_,_,_%29.md)
  Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [func CFPlugInRegisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginregisterplugintype%28_,_%29.md)
  Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](./cfpluginunregisterfactory%28_%29.md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginunregisterplugintype%28_,_%29.md)
  Removes the given type from a plug-in’s list of registered types.
### CFPlugIn Miscellaneous Functions
- [func CFPlugInAddInstanceForFactory(CFUUID!)](./cfpluginaddinstanceforfactory%28_%29.md)
  Registers a new instance of a type with `CFPlugIn`.
- [func CFPlugInFindFactoriesForPlugInType(CFUUID!) -> CFArray!](./cfpluginfindfactoriesforplugintype%28_%29.md)
  Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
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
### Callbacks
- [typealias CFPlugInDynamicRegisterFunction](./cfplugindynamicregisterfunction.md)
  A callback which provides a plug-in the opportunity to dynamically register its types with a host.
- [typealias CFPlugInFactoryFunction](./cfpluginfactoryfunction.md)
  Callback function that a plug-in author must implement to create a plug-in instance.
- [typealias CFPlugInUnloadFunction](./cfpluginunloadfunction.md)
  Callback function that is called, if present, just before a plug-in’s code is unloaded.
### Constants
- [Information Property List Keys](./cfplugin-information-property-list-keys.md)
  A plug-in’s information property list can contain these keys used for registering types, factories, and interfaces.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugin)*