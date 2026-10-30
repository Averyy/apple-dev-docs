# OrgDevice.Relationships

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

The relationships you include in the request, and those that you can operate on.

**Availability**:
- Apple School Manager API 1.8+

## Declaration

```
object OrgDevice.Relationships
```

## Topics

### Dictionaries
- [object OrgDevice.Relationships.ActivationLockStatus](./relationships-data.dictionary/activationlockstatus-data.dictionary.md)
- [object OrgDevice.Relationships.AppleCareCoverage](./relationships-data.dictionary/applecarecoverage-data.dictionary.md)
- [object OrgDevice.Relationships.AssignedServer](./relationships-data.dictionary/assignedserver-data.dictionary.md)
  The links that describe the relationship between the resources.

## Properties

- `assignedServer` (OrgDevice.Relationships.AssignedServer): The relationship representing a device and its assigned device management service.
- `appleCareCoverage` (OrgDevice.Relationships.AppleCareCoverage): The relationship representing a device and its AppleCare Coverage.
- `activationLockStatus` (OrgDevice.Relationships.ActivationLockStatus): The relationship representing a device and its Activation Lock status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/orgdevice/relationships-data.dictionary)*