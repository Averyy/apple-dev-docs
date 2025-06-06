# SecKeychainSetUserInteractionAllowed(_:)

**Framework**: Security  
**Kind**: func

Enables or disables the user interface for keychain services functions that automatically display a user interface.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainSetUserInteractionAllowed(_ state: Bool) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Certain keychain services functions that require the presence of a keychain automatically display a  dialog if there is none. Functions that require the keychain to be unlocked automatically display the  dialog. The [`SecKeychainSetUserInteractionAllowed(_:)`](seckeychainsetuserinteractionallowed(_:).md) function enables you to control whether these functions display a user interface. By default, user interaction is permitted.

If you are writing an application that must run unattended on a server, you may wish to disable the user interface so that any subsequent keychain calls that normally bring up the unlock UI will instead return immediately with an [`errSecInteractionRequired`](errsecinteractionrequired.md) result). In this case you must programmatically create a keychain or unlock the keychain when necessary.

##### Special Considerations

If you disable user interaction before calling a Keychain Services function, be sure to reenable it when you are finished. Failure to reenable user interaction will affect other clients of the Keychain Services.

## Parameters

- `state`: A flag that indicates whether the keychain services will display a user interface. If you pass  , user interaction is allowed. This is the default value. If  , keychain services functions that normally display a user interface will instead return an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetuserinteractionallowed(_:))*