# Identification.PayloadIdentification

**Framework**: Device Management  
**Kind**: dictionary

The dictionary containing details about the user.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Identification.PayloadIdentification
```

## Properties

- `AuthMethod` (string) *(required)*: The authorization method. Either the profile contains the password or the user provides it.
- `EmailAddress` (string) *(required)*: The address for the account.
- `FullName` (string) *(required)*: The full name of the account.
- `Password` (string) *(required)*: The password for the account. Required when the `AuthMethod` is `Password`.
- `Prompt` (string): The custom instructions for the user, if needed.
- `PromptMessage` (string): The additional descriptive text for the user prompt.
- `UserName` (string) *(required)*: The UNIX user name for the accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/identification/payloadidentification-data.dictionary)*