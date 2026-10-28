# accountType(withAccountTypeIdentifier:)

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Returns an account type that matches the specified identifier.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
func accountType(withAccountTypeIdentifier typeIdentifier: String!) -> ACAccountType!
```

```objc
- (ACAccountType *) accountTypeWithAccountTypeIdentifier:(NSString *) typeIdentifier;
```

## Return Value

An account type that matches `typeIdentifier`.

## Parameters

- `typeIdentifier`: The account type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/accounttype(withaccounttypeidentifier:))*