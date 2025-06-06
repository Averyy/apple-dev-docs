# ACErrorCredentialItemNotFound

**Framework**: Accounts  
**Kind**: var

Error code that indicates a credential item wasn’t saved because it couldn’t be found.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
var ACErrorCredentialItemNotFound: ACErrorCode { get }
```

## See Also

- [var ACErrorUnknown: ACErrorCode](acerrorunknown.md)
  Error code that indicates an unknown error occurred.
- [var ACErrorAccountMissingRequiredProperty: ACErrorCode](acerroraccountmissingrequiredproperty.md)
  Error code that indicates an account wasn’t saved because a required property is missing.
- [var ACErrorAccountAuthenticationFailed: ACErrorCode](acerroraccountauthenticationfailed.md)
  Error code that indicates an account wasn’t saved because authentication of its credential failed.
- [var ACErrorAccountTypeInvalid: ACErrorCode](acerroraccounttypeinvalid.md)
  Error code that indicates an account wasn’t saved because its account type is invalid.
- [var ACErrorAccountAlreadyExists: ACErrorCode](acerroraccountalreadyexists.md)
  Error code that indicates an account wasn’t added because it already exists.
- [var ACErrorAccountNotFound: ACErrorCode](acerroraccountnotfound.md)
  Error code that indicates an account wasn’t deleted because it couldn’t be found.
- [var ACErrorPermissionDenied: ACErrorCode](acerrorpermissiondenied.md)
  Error code that indicates the operation failed because the application doesn’t have permission to perform the operation.
- [var ACErrorAccessInfoInvalid: ACErrorCode](acerroraccessinfoinvalid.md)
  Error code that indicates the client’s access info dictionary has incorrect or missing values.
- [var ACErrorClientPermissionDenied: ACErrorCode](acerrorclientpermissiondenied.md)
  Error code that indicates the client doesn’t have access to the requested data.
- [var ACErrorAccessDeniedByProtectionPolicy: ACErrorCode](acerroraccessdeniedbyprotectionpolicy.md)
  Error code that indicates due to the current protection policy, the credentials couldn’t be fetched.
- [var ACErrorCredentialNotFound: ACErrorCode](acerrorcredentialnotfound.md)
  Error code that indicates no credentials were found.
- [var ACErrorFetchCredentialFailed: ACErrorCode](acerrorfetchcredentialfailed.md)
  Error code that indicates the credentials couldn’t be fetched from Keychain.
- [var ACErrorStoreCredentialFailed: ACErrorCode](acerrorstorecredentialfailed.md)
  Error code that indicates the credentials couldn’t be stored in Keychain.
- [var ACErrorRemoveCredentialFailed: ACErrorCode](acerrorremovecredentialfailed.md)
  Error code that indicates the credentials couldn’t be removed from Keychain.
- [var ACErrorUpdatingNonexistentAccount: ACErrorCode](acerrorupdatingnonexistentaccount.md)
  Error code that indicates an account save failed because the account being updated has been removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acerrorcredentialitemnotfound)*