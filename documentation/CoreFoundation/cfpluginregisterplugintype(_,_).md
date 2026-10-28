# CFPlugInRegisterPlugInType(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Registers a type and its corresponding factory function with a `CFPlugIn` object.

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
func CFPlugInRegisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Bool
```

```c
extern Boolean CFPlugInRegisterPlugInType(CFUUIDRef factoryUUID, CFUUIDRef typeUUID);
```

## Return Value

`true` if the factory function was successfully registered, otherwise `false`.

## Discussion

This function is used by a plug-in or host when performing dynamic registration.

## Parameters

- `factoryUUID`: The `CFUUID` object representing the factory function that can create the type being registered.
- `typeUUID`: The UUID type to register.

## See Also

### Registration
- [func CFPlugInRegisterFactoryFunction(CFUUID!, CFPlugInFactoryFunction!) -> Bool](./cfpluginregisterfactoryfunction%28_,_%29.md)
  Registers a factory function and its UUID with a `CFPlugIn` object.
- [func CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Bool](./cfpluginregisterfactoryfunctionbyname%28_,_,_%29.md)
  Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](./cfpluginunregisterfactory%28_%29.md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginunregisterplugintype%28_,_%29.md)
  Removes the given type from a plug-in’s list of registered types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginregisterplugintype(_:_:))*