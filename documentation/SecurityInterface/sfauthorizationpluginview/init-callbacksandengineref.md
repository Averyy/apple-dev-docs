# init(callbacks:andEngineRef:)

**Framework**: Security Interface  
**Kind**: init

Initializes a new authorization plug-in view with the specified callbacks and authorization engine handle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(callbacks: UnsafePointer<AuthorizationCallbacks>!, andEngineRef engineRef: AuthorizationEngineRef!)
```

#### Return Value

An initialized `SFAuthorizationPluginView` instance.

## Parameters

- `callbacks`: The structure of type   provided to the authorization plug-in in its   function.
- `engineRef`: The handle of type   provided to the authorization plug-in in its MechanismCreate function.

## See Also

- [Authorization Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/init(callbacks:andengineref:))*