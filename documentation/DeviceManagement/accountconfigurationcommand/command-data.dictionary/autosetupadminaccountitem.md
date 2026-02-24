# AccountConfigurationCommand.Command.AutoSetupAdminAccountItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the administrator account to create with Setup Assistant, which uses the first element and ignores additional elements.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object AccountConfigurationCommand.Command.AutoSetupAdminAccountItem
```

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

## Properties

- `fullName` (string): The full name of the user, which defaults to `shortName` if not specified.
- `hidden` (boolean): If `true`, this sets the account attribute to make the account hidden in the Login Window and Users & Groups.
- `passwordHash` (data): Data that contains the pre-created salted PBKDF2 SHA512 password hash for the account.
- `shortName` (string) *(required)*: The short name of the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountconfigurationcommand/command-data.dictionary/autosetupadminaccountitem)*