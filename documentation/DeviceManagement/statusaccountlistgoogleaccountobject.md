# StatusAccountListGoogleAccountObject

**Framework**: Device Management  
**Kind**: dictionary

A Google account.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object StatusAccountListGoogleAccountObject
```

## Properties

- `_removed` (boolean): If `true`, the device removed the account and the status item object only contains this key and the `identifier` key.
- `are-calendars-enabled` (boolean): A Boolean value that indicates whether the Calendar app displays calendars and events for this account.
- `are-contacts-enabled` (boolean): A Boolean value that indicates whether the Contacts app displays contacts for this account.
- `are-notes-enabled` (boolean): A Boolean value that indicates whether the Notes app displays notes for this account.
- `declaration-identifier` (string): The identifier of the declaration that installed the account. Only present if a declaration installed the account.
- `identifier` (string) *(required)*: The unique identifier for the account.
- `is-mail-enabled` (boolean): A Boolean value that indicates whether the Mail app displays mail for this account.
- `username` (string): The user name for the account.
- `visible-name` (string): The name of the account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistgoogleaccountobject)*