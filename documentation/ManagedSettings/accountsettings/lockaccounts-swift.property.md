# lockAccounts

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to prevent the user from changing their account information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var lockAccounts: Bool? { get set }
```

#### Discussion

Your app can enable or disable changes to the user’s account settings. The default value is `nil`.

## See Also

### Constraining accounts
- [static let lockAccounts: SettingMetadata<Bool>](./lockaccounts-swift.type.property.md)
  A description of the setting that controls whether a user can modify their account information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/accountsettings/lockaccounts-swift.property)*