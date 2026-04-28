# StatusAccountListMailOutgoingAccountObject

**Framework**: Device Management  
**Kind**: dictionary

A status report of the client’s outgoing Mail account details.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusAccountListMailOutgoingAccountObject
```

## Properties

- `_removed` (boolean): If `true`, the account is removed and the status item object only contains this key and the `identifier` key.
- `declaration-identifier` (string): The identifier of the declaration that installed the account. Only present if a declaration installed the account.
- `hostname` (string): The server host name for the account.
- `identifier` (string) *(required)*: The unique identifier for the account.
- `port` (integer): The server port for the account.
- `username` (string): The user name for the account.
- `visible-name` (string): The name of the account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusaccountlistmailoutgoingaccountobject)*