# AuthorizationMechanismRef

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A handle passed by the plug-in to the authorization engine when creating an instance of a mechanism.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
typedef void * AuthorizationMechanismRef;
```

#### Discussion

Your [`MechanismCreate`](./authorizationplugininterface/mechanismcreate.md) function assigns this value and returns it to the authorization engine. The authorization engine passes this reference back to you in any subsequent calls to your [`MechanismInvoke`](./authorizationplugininterface/mechanisminvoke.md), [`MechanismDeactivate`](./authorizationplugininterface/mechanismdeactivate.md), and [`MechanismDestroy`](./authorizationplugininterface/mechanismdestroy.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationmechanismref)*