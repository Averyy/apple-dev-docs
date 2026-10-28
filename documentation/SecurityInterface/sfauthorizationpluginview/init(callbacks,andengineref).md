# init(callbacks:andEngineRef:)

**Framework**: Security Interface  
**Kind**: init  
**Role**: Initializer

Initializes a new authorization plug-in view with the specified callbacks and authorization engine handle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(callbacks: UnsafePointer<AuthorizationCallbacks>!, andEngineRef engineRef: AuthorizationEngineRef!)
```

```objc
- (id) initWithCallbacks:(const AuthorizationCallbacks *) callbacks andEngineRef:(AuthorizationEngineRef) engineRef;
```

## Return Value

An initialized `SFAuthorizationPluginView` instance.

## Parameters

- `callbacks`: The structure of type [`AuthorizationCallbacks`](../../Security/authorizationcallbacks.md) provided to the authorization plug-in in its [`AuthorizationPluginCreate`](../../Security/authorizationplugincreate.md) function.
- `engineRef`: The handle of type [`AuthorizationEngineRef`](../../Security/authorizationengineref.md) provided to the authorization plug-in in its MechanismCreate function.

## See Also

### Related Documentation
- [Authorization Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995)


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/init(callbacks:andengineref:))*