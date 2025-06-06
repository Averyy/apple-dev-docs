# CFPlugInRegisterFactoryFunction(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Registers a factory function and its UUID with a `CFPlugIn` object.

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
func CFPlugInRegisterFactoryFunction(_ factoryUUID: CFUUID!, _ func: CFPlugInFactoryFunction!) -> Bool
```

#### Return Value

`true` if the factory function was successfully registered, otherwise `false`.

#### Discussion

This function is used by a plug-in or host when performing dynamic registration.

## Parameters

- `factoryUUID`: The   object representing the factory function to register.
- `func`: The factory function pointer to register.

## See Also

- [func CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Bool](cfpluginregisterfactoryfunctionbyname(_:_:_:).md)
  Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [func CFPlugInRegisterPlugInType(CFUUID!, CFUUID!) -> Bool](cfpluginregisterplugintype(_:_:).md)
  Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](cfpluginunregisterfactory(_:).md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](cfpluginunregisterplugintype(_:_:).md)
  Removes the given type from a plug-in’s list of registered types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginregisterfactoryfunction(_:_:))*