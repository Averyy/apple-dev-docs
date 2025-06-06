# CFPlugInRegisterFactoryFunctionByName(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.

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
func CFPlugInRegisterFactoryFunctionByName(_ factoryUUID: CFUUID!, _ plugIn: CFPlugIn!, _ functionName: CFString!) -> Bool
```

#### Return Value

`true` if the factory function was successfully registered, otherwise `false`.

#### Discussion

This function is used by a plug-in or host when performing dynamic registration.

## Parameters

- `factoryUUID`: The   object representing the factory function to register.
- `plugIn`: The plug-in containing  .
- `functionName`: The name of the factory function to register.

## See Also

- [func CFPlugInRegisterFactoryFunction(CFUUID!, CFPlugInFactoryFunction!) -> Bool](cfpluginregisterfactoryfunction(_:_:).md)
  Registers a factory function and its UUID with a `CFPlugIn` object.
- [func CFPlugInRegisterPlugInType(CFUUID!, CFUUID!) -> Bool](cfpluginregisterplugintype(_:_:).md)
  Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [func CFPlugInUnregisterFactory(CFUUID!) -> Bool](cfpluginunregisterfactory(_:).md)
  Removes the given function from a plug-in’s list of registered factory functions.
- [func CFPlugInUnregisterPlugInType(CFUUID!, CFUUID!) -> Bool](cfpluginunregisterplugintype(_:_:).md)
  Removes the given type from a plug-in’s list of registered types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpluginregisterfactoryfunctionbyname(_:_:_:))*