# CFPlugInRegisterFactoryFunction(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Registers a factory function and its UUID with a `CFPlugIn` object.

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
func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ func: CFPlugInFactoryFunction!) -> Bool
```

```c
extern Boolean CFPlugInRegisterFactoryFunction(CFUUIDRef factoryUUID, CFPlugInFactoryFunction func);
```

#### Return Value

`true` if the factory function was successfully registered, otherwise `false`.

#### Discussion

This function is used by a plug-in or host when performing dynamic registration.

## Parameters

- `factoryUUID`: The `CFUUID` object representing the factory function to register.
- `func`: The factory function pointer to register.

## See Also

### Registration
- [func CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Bool](./cfpluginregisterfactoryfunctionbyname%28_,_,_%29.md)
  Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [func CFPlugInRegisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginregisterplugintype%28_,_%29.md)
  Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](./cfpluginunregisterfactory%28_%29.md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginunregisterplugintype%28_,_%29.md)
  Removes the given type from a plug-in’s list of registered types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginregisterfactoryfunction(_:_:))*