# Identification.PayloadIdentification

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary containing details about the user.

**Availability**:
- macOS 10.7+ - Deprecated in 15.4

## Declaration

```
object Identification.PayloadIdentification
```

## Properties

- `AuthMethod` (string) *(required)* *(deprecated)*: The authorization method. Either the profile contains the password or the user provides it.

  Deprecated: macOS 15.4+

  **Allowed Values**: `Password`, `UserEnteredPassword`
- `EmailAddress` (string) *(required)* *(deprecated)*: The address for the account.

  Deprecated: macOS 15.4+
- `FullName` (string) *(required)* *(deprecated)*: The full name of the account.

  Deprecated: macOS 15.4+
- `Password` (string) *(required)* *(deprecated)*: The password for the account. Required when the `AuthMethod` is `Password`.

  Deprecated: macOS 15.4+
- `Prompt` (string) *(deprecated)*: The custom instructions for the user, if needed.

  Deprecated: macOS 15.4+
- `PromptMessage` (string) *(deprecated)*: The additional descriptive text for the user prompt.

  Deprecated: macOS 15.4+
- `UserName` (string) *(required)* *(deprecated)*: The UNIX user name for the accounts.

  Deprecated: macOS 15.4+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/identification/payloadidentification-data.dictionary)*