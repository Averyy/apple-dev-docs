# AccountConfigurationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to create and configure a local administrator account on a device.

**Availability**:
- macOS 10.11+

## Declaration

```swift
object AccountConfigurationCommand.Command
```

## Topics

### Objects
- [object AccountConfigurationCommand.Command.AutoSetupAdminAccountItem](accountconfigurationcommand/command-data.dictionary/autosetupadminaccountitem.md)
  A dictionary that describes the administrator account to create with Setup Assistant, which uses the first element and ignores additional elements.

## Properties

- `AutoSetupAdminAccounts` ([AccountConfigurationCommand.Command.AutoSetupAdminAccountItem]): A dictionary that describes the administrator account to create with Setup Assistant, which uses the first element and ignores additional elements.
- `DontAutoPopulatePrimaryAccountInfo` (boolean): If `true`, Setup Assistant ignores the primary account information and requires the user to enter that information. If `false`, Setup Assistant prefills the Full Name field with `PrimaryAccountFullName` and the User Name field with `PrimaryAccountUserName`. Available: macOS 10.15+
- `LockPrimaryAccountInfo` (boolean): If `true`, and you provide values for `PrimaryAccountFullName` or `PrimaryAccountUserName`, Setup Assistant disables editing for the corresponding fields. `DontAutoPopulatePrimaryAccountInfo` must also be 0 (or missing). If the user’s password is also available from authentication through ConfigurationURL, Setup Assistant automatically creates the primary account with that information and skips showing the user interface to view or edit these fields. Available: macOS 10.15+
- `ManagedLocalUserShortName` (string): If present, this is the short name of the local account to manage, which can also be the account that results from setting `AutoSetupAdminAccounts` to `true`. Otherwise, only the local account that Setup Assistant creates is a managed account. Available: macOS 11+
- `PrimaryAccountFullName` (string): The full name for the primary account. If present, Setup Assistant uses this value to prefill the Full Name field. However, Setup Assistant ignores this value if `DontAutoPopulatePrimaryAccountInfo` is `true`. Available: macOS 10.15+
- `PrimaryAccountUserName` (string): The account name for the primary account. If present, Setup Assistant uses this value to prefill the User Name field. However, Setup Assistant ignores this value if `DontAutoPopulatePrimaryAccountInfo` is `true`. Available: macOS 10.15+
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `SetPrimarySetupAccountAsRegularUser` (boolean): If `true`, Setup Assistant creates the primary accounts as regular users, and you must specify a value for `AutoSetupAdminAccounts`.
- `SkipPrimarySetupAccountCreation` (boolean): If `true`, Setup Assistant skips the user interface for setting up primary accounts and disables autologin. If `true`, you must specify a value for `AutoSetupAdminAccounts`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountconfigurationcommand/command-data.dictionary)*