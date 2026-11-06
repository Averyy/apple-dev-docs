# WebhookEventType

**Framework**: AppleBusinessAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent the types of events a webhook can subscribe to.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
string WebhookEventType
```

## Possible Values

- `ORG_DEVICE_ATTRIBUTE_CHANGED`
- `ORG_DEVICE_ATTRIBUTE_MIGRATION_DETAILS_CHANGED`
- `ORG_DEVICE_RELATIONSHIP_ASSIGNED_SERVER_CHANGED`
- `ORG_DEVICE_RELATIONSHIP_WARRANTY_CHANGED`

## Mentions

- [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md)

## Discussion

- Possible Values

  - ORG_DEVICE_ATTRIBUTE_CHANGED: An attribute of a device changed.
  - ORG_DEVICE_ATTRIBUTE_MIGRATION_DETAILS_CHANGED: The device management service migration details of a device changed.
  - ORG_DEVICE_RELATIONSHIP_ASSIGNED_SERVER_CHANGED: The device management service assigned to a device changed.
  - ORG_DEVICE_RELATIONSHIP_WARRANTY_CHANGED: The AppleCare coverage of a device changed.

For the data each event contains, see [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md).

## See Also

### Type Aliases
- [type OrgDeviceActivityType](./orgdeviceactivitytype.md)
  Strings that represent organization device activities.
- [type AppleCareCoveragePaymentType](./applecarecoveragepaymenttype.md)
  Strings that represent AppleCare coverage payment types.
- [type AppleCareCoverageStatus](./applecarecoveragestatus.md)
  Strings that represent AppleCare coverage status.
- [type UserStatus](./userstatus.md)
  Strings that represent user statuses.
- [type UserPhoneNumberType](./userphonenumbertype.md)
  Strings that represent phone number types.
- [type UserGroupStatus](./usergroupstatus.md)
  Strings that represent user group statuses.
- [type UserGroupType](./usergrouptype.md)
  Strings that represent user group types.
- [type SupportedOS](./supportedos.md)
  The supported operating systems for an app.
- [type BlueprintStatus](./blueprintstatus.md)
  The status of a Blueprint.
- [type ConfigurationType](./configurationtype.md)
  The type of Configuration profile.
- [type ConfigurationPlatform](./configurationplatform.md)
  The platform that a Configuration targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookeventtype)*