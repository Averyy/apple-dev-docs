# SecKeychainCallbackInfo

**Framework**: Security  
**Kind**: struct

Information about a keychain event that keychain services deliver to your app via a callback function.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainCallbackInfo
```

#### Overview

This structure contains information about the keychain event of which your application wants to be notified. Keychain services pass a pointer to this structure in the `info` parameter of your callback function. For information on how to write a keychain event callback function, see [`SecKeychainCallback`](seckeychaincallback.md).

## Topics

### Instance Properties
- [var item: Unmanaged<SecKeychainItem>](seckeychaincallbackinfo/item.md)
  A reference to the keychain item in which the event occurred. If the event did not involve an item, this field is not valid.
- [var keychain: Unmanaged<SecKeychain>](seckeychaincallbackinfo/keychain.md)
  A reference to the keychain in which the event occurred. If the event did not involve a keychain, this field is not valid.
- [var pid: pid_t](seckeychaincallbackinfo/pid.md)
  The ID of the process that generated this event.
- [var version: UInt32](seckeychaincallbackinfo/version.md)
  The version of this structure.
### Initializers
- [init(version: UInt32, item: Unmanaged<SecKeychainItem>, keychain: Unmanaged<SecKeychain>, pid: pid_t)](seckeychaincallbackinfo/init(version:item:keychain:pid:).md)
  Creates a new keychain callback information structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincallbackinfo)*