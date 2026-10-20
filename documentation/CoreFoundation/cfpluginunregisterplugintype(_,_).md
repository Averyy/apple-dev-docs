# CFPlugInUnregisterPlugInType(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes the given type from a plug-in’s list of registered types.

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
func CFPlugInUnregisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Bool
```

```c
extern Boolean CFPlugInUnregisterPlugInType(CFUUIDRef factoryUUID, CFUUIDRef typeUUID);
```

#### Return Value

`true` if the factory function was successfully unregistered, otherwise `false`.

#### Discussion

Used by a plug-in or host when performing dynamic registration.

## Parameters

- `factoryUUID`: The `CFUUID` object representing the factory function for the type to unregister.
- `typeUUID`: The UUID type to unregister.

## See Also

### Registration
- [func CFPlugInRegisterFactoryFunction(CFUUID!, CFPlugInFactoryFunction!) -> Bool](./cfpluginregisterfactoryfunction%28_,_%29.md)
  Registers a factory function and its UUID with a `CFPlugIn` object.
- [func CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Bool](./cfpluginregisterfactoryfunctionbyname%28_,_,_%29.md)
  Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [func CFPlugInRegisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginregisterplugintype%28_,_%29.md)
  Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](./cfpluginunregisterfactory%28_%29.md)
  Removes the given function from a plug-in’s list of registered factory functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginunregisterplugintype(_:_:))*