# LAContext

**Framework**: Local Authentication  
**Kind**: class

A mechanism for evaluating authentication policies and access controls.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class LAContext
```

#### Overview

You use an authentication context to evaluate the user’s identity, either with biometrics like Touch ID or Face ID, or by supplying the device passcode. The context handles user interaction, and also interfaces to the Secure Enclave, the underlying hardware element that manages biometric data. You create and configure the context, and ask it to carry out the authentication. You then receive an asynchronous callback, which provides an indication of authentication success or failure, and an error instance that explains the reason for a failure, if any.

> ❗ **Important**:  Include the [`NSFaceIDUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW75) key in your app’s `Info.plist` file if your app allows biometric authentication. Otherwise, authorization requests may fail.

 Include the [`NSFaceIDUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW75) key in your app’s `Info.plist` file if your app allows biometric authentication. Otherwise, authorization requests may fail.

## Topics

### Checking availability
- [func canEvaluatePolicy(LAPolicy, error: NSErrorPointer) -> Bool](lacontext/canevaluatepolicy(_:error:).md)
  Assesses whether authentication can proceed for a given policy.
- [enum LAPolicy](lapolicy.md)
  The set of available local authentication policies.
- [var biometryType: LABiometryType](lacontext/biometrytype.md)
  The type of biometric authentication supported by the device.
- [enum LABiometryType](labiometrytype.md)
  The set of available biometric authentication types.
### Evaluating authentication policies
- [func evaluatePolicy(LAPolicy, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](lacontext/evaluatepolicy(_:localizedreason:reply:).md)
  Evaluates the specified policy.
- [var evaluatedPolicyDomainState: Data?](lacontext/evaluatedpolicydomainstate.md)
  The current state of the evaluated policy domain.
- [var maxBiometryFailures: NSNumber?](lacontext/maxbiometryfailures.md)
  The number of biometric authentication failures after which the context falls back to another mechanism.
### Evaluating access controls
- [func evaluateAccessControl(SecAccessControl, operation: LAAccessControlOperation, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](lacontext/evaluateaccesscontrol(_:operation:localizedreason:reply:).md)
  Evaluates an access control for a given operation.
- [enum LAAccessControlOperation](laaccesscontroloperation.md)
  Operations to be evaluated for access control.
- [var interactionNotAllowed: Bool](lacontext/interactionnotallowed.md)
  A Boolean value indicating whether authentication can be interactive.
### Customizing authentication prompts
- [var localizedReason: String](lacontext/localizedreason.md)
  The localized explanation for authentication shown in the dialog presented to the user.
- [var localizedFallbackTitle: String?](lacontext/localizedfallbacktitle.md)
  The localized title for the fallback button in the dialog presented to the user during authentication.
- [var localizedCancelTitle: String?](lacontext/localizedcanceltitle.md)
  The localized title for the cancel button in the dialog presented to the user during authentication.
### Reusing device unlock state
- [var touchIDAuthenticationAllowableReuseDuration: TimeInterval](lacontext/touchidauthenticationallowablereuseduration.md)
  The duration for which Touch ID authentication reuse is allowable.
- [let LATouchIDAuthenticationMaximumAllowableReuseDuration: TimeInterval](latouchidauthenticationmaximumallowablereuseduration.md)
  The maximum allowable reuse duration.
### Managing credentials
- [func setCredential(Data?, type: LACredentialType) -> Bool](lacontext/setcredential(_:type:).md)
  Sets an application-provided credential to be used when evaluating authentication.
- [func isCredentialSet(LACredentialType) -> Bool](lacontext/iscredentialset(_:).md)
  Returns a Boolean value indicating whether the specified credential type is set.
- [enum LACredentialType](lacredentialtype.md)
  The types of credentials to be used for authentication.
### Invalidating the authentication context
- [func invalidate()](lacontext/invalidate.md)
  Invalidates the authentication context.
### Instance Properties
- [var domainState: LADomainState](lacontext/domainstate.md)
  Contains authentication domain state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Observable](../Observation/Observable.md)
- [ObservableObject](../Combine/ObservableObject.md)

## See Also

- [class LARight](laright.md)
  A grouped set of requirements that gate access to a resource or operation.
- [LARight.State](laright/state-swift.enum.md)
  The possible states for a right during authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext)*