# SecKeychainGetVersion(_:)

**Framework**: Security  
**Kind**: func

Determines the version of keychain services installed on the user’s system.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainGetVersion(_ returnVers: UnsafeMutablePointer<UInt32>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Your application can call the [`SecKeychainGetVersion(_:)`](seckeychaingetversion(_:).md) function to find out which version of keychain services is installed on the user’s system.

## Parameters

- `returnVers`: On return, a pointer to the version number of keychain services installed on the current system. See   for a list of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetversion(_:))*