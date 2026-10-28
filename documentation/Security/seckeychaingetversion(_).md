# SecKeychainGetVersion(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Determines the version of keychain services installed on the user’s system.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecKeychainGetVersion(_ returnVers: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
OSStatus SecKeychainGetVersion(UInt32 *returnVers);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

Your application can call the [`SecKeychainGetVersion(_:)`](./seckeychaingetversion%28_%29.md) function to find out which version of keychain services is installed on the user’s system.

## Parameters

- `returnVers`: On return, a pointer to the version number of keychain services installed on the current system. See `Keychain Settings Version` for a list of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetversion(_:))*