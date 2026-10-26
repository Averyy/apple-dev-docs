# ActivationLockStatus

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents the Activation Lock status of an organization device.

**Availability**:
- Apple School Manager API 1.7+

## Declaration

```
object ActivationLockStatus
```

## Topics

### Dictionaries
- [object ActivationLockStatus.Attributes](./activationlockstatus/attributes-data.dictionary.md)
  Attributes for an organization device’s Activation Lock status.

## Properties

- `attributes` (ActivationLockStatus.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `activationLockStatus`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/activationlockstatus)*