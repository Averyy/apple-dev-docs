# SecKeychainRemoveCallback(_:)

**Framework**: Security  
**Kind**: func

Unregisters your keychain event callback function.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainRemoveCallback(_ callbackFunction: SecKeychainCallback) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Once removed, keychain events are not sent to the owner of the callback.

## Parameters

- `callbackFunction`: The callback function pointer to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainremovecallback(_:))*