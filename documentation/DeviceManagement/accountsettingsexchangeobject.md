# AccountSettingsExchangeObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

If present, configures settings for Exchange accounts.

**Availability**:
- macOS 27.2+

## Declaration

```
object AccountSettingsExchangeObject
```

## Properties

- `AllowEWSRetirementAlerts` (boolean): If `false`, the system doesn’t alert the user that an Exchange account has lost, or is about to lose, access because Microsoft is ending support for Exchange Web Services. Only applies to Exchange accounts installed by an organization.

  **Default**: `true`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountsettingsexchangeobject)*