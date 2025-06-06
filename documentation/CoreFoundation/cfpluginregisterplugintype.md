# CFPlugInRegisterPlugInType(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Registers a type and its corresponding factory function with a `CFPlugIn` object.

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
func CFPlugInRegisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Bool
```

#### Return Value

`true` if the factory function was successfully registered, otherwise `false`.

#### Discussion

This function is used by a plug-in or host when performing dynamic registration.

## Parameters

- `factoryUUID`: The   object representing the factory function that can create the type being registered.
- `typeUUID`: The UUID type to register.

## See Also

- [func CFPlugInRegisterFactoryFunction(CFUUID!, CFPlugInFactoryFunction!) -> Bool](cfpluginregisterfactoryfunction(_:_:).md)
  Registers a factory function and its UUID with a `CFPlugIn` object.
- [func CFPlugInRegisterFactoryFunctionByName(CFUUID!, CFPlugIn!, CFString!) -> Bool](cfpluginregisterfactoryfunctionbyname(_:_:_:).md)
  Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](cfpluginunregisterfactory(_:).md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](cfpluginunregisterplugintype(_:_:).md)
  Removes the given type from a plug-in’s list of registered types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginregisterplugintype(_:_:))*