# Identification.PayloadIdentification

**Framework**: Device Management  
**Kind**: dictionary

The dictionary containing details about the user.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object Identification.PayloadIdentification
```

## Properties

- `AuthMethod` (string) *(required)*: The authorization method. Either the profile contains the password or the user provides it. Deprecated: macOS 15.4+
- `EmailAddress` (string) *(required)*: The address for the account. Deprecated: macOS 15.4+
- `FullName` (string) *(required)*: The full name of the account. Deprecated: macOS 15.4+
- `Password` (string) *(required)*: The password for the account. Required when the `AuthMethod` is `Password`. Deprecated: macOS 15.4+
- `Prompt` (string): The custom instructions for the user, if needed. Deprecated: macOS 15.4+
- `PromptMessage` (string): The additional descriptive text for the user prompt. Deprecated: macOS 15.4+
- `UserName` (string) *(required)*: The UNIX user name for the accounts. Deprecated: macOS 15.4+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/identification/payloadidentification-data.dictionary)*