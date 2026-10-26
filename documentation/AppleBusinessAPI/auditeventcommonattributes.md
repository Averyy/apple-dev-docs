# AuditEventCommonAttributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The common attributes for all audit events.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object AuditEventCommonAttributes
```

## Properties

- `eventDateTime` (date-time): Timestamp when the event occurred (ISO8601 format, UTC).
- `type` (AuditEventType) *(required)*: The type of event that occurred.
- `category` (AuditEventCategory): The category of the event.
- `actorType` (AuditEventActorType): The type of entity that performed the action.
- `actorId` (string): Unique identifier of the actor.
- `actorName` (string): Display name of the actor. Optional, may not be populated for all events.
- `subjectType` (AuditEventSubjectType): The type of entity that was affected.
- `subjectId` (string): Unique identifier of the subject.
- `subjectName` (string): Display name of the subject. Optional, may not be populated for all events.
- `outcome` (AuditEventOutcome): The result of the action. Optional, may not be populated for all events.
- `groupId` (string): Identifier for grouping related events. Optional, may not be populated for all events.
- `eventDataPropertyKey` (string): Property key for event-specific data.

## Relationships

### Inherited By
- [AuditEventAccountAddedAttributes](./auditeventaccountaddedattributes.md)
- [AuditEventAccountDeletedAttributes](./auditeventaccountdeletedattributes.md)
- [AuditEventAccountImageRemovedAttributes](./auditeventaccountimageremovedattributes.md)
- [AuditEventAccountImageReplacedAttributes](./auditeventaccountimagereplacedattributes.md)
- [AuditEventAccountImageSetAttributes](./auditeventaccountimagesetattributes.md)
- [AuditEventAccountPasswordChangedAttributes](./auditeventaccountpasswordchangedattributes.md)
- [AuditEventAccountRoleLocationChangedAttributes](./auditeventaccountrolelocationchangedattributes.md)
- [AuditEventApiAccountCreatedWithKeyAttributes](./auditeventapiaccountcreatedwithkeyattributes.md)
- [AuditEventApiAccountCreatedWithoutKeyAttributes](./auditeventapiaccountcreatedwithoutkeyattributes.md)
- [AuditEventApiAccountDeletedAttributes](./auditeventapiaccountdeletedattributes.md)
- [AuditEventApiAccountKeyGeneratedAttributes](./auditeventapiaccountkeygeneratedattributes.md)
- [AuditEventApiAccountKeyRevokedAttributes](./auditeventapiaccountkeyrevokedattributes.md)
- [AuditEventApiAccountNameChangedAttributes](./auditeventapiaccountnamechangedattributes.md)
- [AuditEventApiAccountRoleLocationChangedAttributes](./auditeventapiaccountrolelocationchangedattributes.md)
- [AuditEventAppleServicesSettingsUpdatedAttributes](./auditeventappleservicessettingsupdatedattributes.md)
- [AuditEventBatchPasswordResetInitiatedAttributes](./auditeventbatchpasswordresetinitiatedattributes.md)
- [AuditEventCollectionCreatedAttributes](./auditeventcollectioncreatedattributes.md)
- [AuditEventCollectionDeletedAttributes](./auditeventcollectiondeletedattributes.md)
- [AuditEventCollectionUpdatedAttributes](./auditeventcollectionupdatedattributes.md)
- [AuditEventConfigSettingsCreatedAttributes](./auditeventconfigsettingscreatedattributes.md)
- [AuditEventConfigSettingsDeletedAttributes](./auditeventconfigsettingsdeletedattributes.md)
- [AuditEventConfigSettingsUpdatedAttributes](./auditeventconfigsettingsupdatedattributes.md)
- [AuditEventDeviceAddedToOrgAttributes](./auditeventdeviceaddedtoorgattributes.md)
- [AuditEventDeviceAssignedToServerAttributes](./auditeventdeviceassignedtoserverattributes.md)
- [AuditEventDeviceIsErasedAttributes](./auditeventdeviceiserasedattributes.md)
- [AuditEventDeviceRemovedFromOrgAttributes](./auditeventdeviceremovedfromorgattributes.md)
- [AuditEventDeviceUnassignedFromServerAttributes](./auditeventdeviceunassignedfromserverattributes.md)
- [AuditEventDomainAddedAttributes](./auditeventdomainaddedattributes.md)
- [AuditEventDomainFederationDisabledAttributes](./auditeventdomainfederationdisabledattributes.md)
- [AuditEventDomainFederationEnabledAttributes](./auditeventdomainfederationenabledattributes.md)
- [AuditEventDomainRemovedAttributes](./auditeventdomainremovedattributes.md)
- [AuditEventDomainVerifiedAttributes](./auditeventdomainverifiedattributes.md)
- [AuditEventExternalAccountAssociatedAttributes](./auditeventexternalaccountassociatedattributes.md)
- [AuditEventExternalAccountDisassociatedAttributes](./auditeventexternalaccountdisassociatedattributes.md)
- [AuditEventExternalAccountInvitedAttributes](./auditeventexternalaccountinvitedattributes.md)
- [AuditEventIdpAccountSyncDisabledAttributes](./auditeventidpaccountsyncdisabledattributes.md)
- [AuditEventIdpAccountSyncEnabledAttributes](./auditeventidpaccountsyncenabledattributes.md)
- [AuditEventIdpCreatedAttributes](./auditeventidpcreatedattributes.md)
- [AuditEventIdpDeletedAttributes](./auditeventidpdeletedattributes.md)
- [AuditEventIdpUpdatedAttributes](./auditeventidpupdatedattributes.md)
- [AuditEventRoleCreatedAttributes](./auditeventrolecreatedattributes.md)
- [AuditEventRoleUpdatedAttributes](./auditeventroleupdatedattributes.md)
- [AuditEventSubjectHasApplecarePurchaseAddedAttributes](./auditeventsubjecthasapplecarepurchaseaddedattributes.md)
- [AuditEventSubjectHasApplecarePurchaseRemovedAttributes](./auditeventsubjecthasapplecarepurchaseremovedattributes.md)
- [AuditEventSubjectHasIcloudStoragePurchaseAddedAttributes](./auditeventsubjecthasicloudstoragepurchaseaddedattributes.md)
- [AuditEventSubjectHasIcloudStoragePurchaseRemovedAttributes](./auditeventsubjecthasicloudstoragepurchaseremovedattributes.md)
- [AuditEventSubscriptionCreatedAttributes](./auditeventsubscriptioncreatedattributes.md)
- [AuditEventSubscriptionDeletedAttributes](./auditeventsubscriptiondeletedattributes.md)
- [AuditEventSubscriptionUpdatedAttributes](./auditeventsubscriptionupdatedattributes.md)
- [AuditEventTermsAcceptedAttributes](./auditeventtermsacceptedattributes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/auditeventcommonattributes)*