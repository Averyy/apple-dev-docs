# CFPlugInRegisterFactoryFunctionByName(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.

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
func CFPlugInRegisterFactoryFunctionByName(_ factoryUUID: CFUUID!, _ plugIn: CFPlugIn!, _ functionName: CFString!) -> Bool
```

```c
extern Boolean CFPlugInRegisterFactoryFunctionByName(CFUUIDRef factoryUUID, CFPlugInRef plugIn, CFStringRef functionName);
```

## Return Value

`true` if the factory function was successfully registered, otherwise `false`.

## Discussion

This function is used by a plug-in or host when performing dynamic registration.

## Parameters

- `factoryUUID`: The `CFUUID` object representing the factory function to register.
- `plugIn`: The plug-in containing `functionName`.
- `functionName`: The name of the factory function to register.

## See Also

### Registration
- [func CFPlugInRegisterFactoryFunction(CFUUID!, CFPlugInFactoryFunction!) -> Bool](./cfpluginregisterfactoryfunction%28_,_%29.md)
  Registers a factory function and its UUID with a `CFPlugIn` object.
- [func CFPlugInRegisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginregisterplugintype%28_,_%29.md)
  Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](./cfpluginunregisterfactory%28_%29.md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](./cfpluginunregisterplugintype%28_,_%29.md)
  Removes the given type from a plug-in’s list of registered types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginregisterfactoryfunctionbyname(_:_:_:))*