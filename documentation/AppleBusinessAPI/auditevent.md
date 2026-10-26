# AuditEvent

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents an audit event resource.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object AuditEvent
```

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `auditEvents`
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `attributes` ((AuditEventDeviceAddedToOrgAttributes | AuditEventDeviceRemovedFromOrgAttributes | AuditEventDeviceAssignedToServerAttributes | AuditEventDeviceUnassignedFromServerAttributes | AuditEventSubjectHasIcloudStoragePurchaseAddedAttributes | AuditEventSubjectHasIcloudStoragePurchaseRemovedAttributes | AuditEventSubjectHasApplecarePurchaseAddedAttributes | AuditEventSubjectHasApplecarePurchaseRemovedAttributes | AuditEventDeviceIsErasedAttributes | AuditEventConfigSettingsCreatedAttributes | AuditEventConfigSettingsUpdatedAttributes | AuditEventConfigSettingsDeletedAttributes | AuditEventCollectionCreatedAttributes | AuditEventCollectionUpdatedAttributes | AuditEventCollectionDeletedAttributes | AuditEventSubscriptionCreatedAttributes | AuditEventSubscriptionUpdatedAttributes | AuditEventSubscriptionDeletedAttributes | AuditEventAccountRoleLocationChangedAttributes | AuditEventAccountAddedAttributes | AuditEventAccountDeletedAttributes | AuditEventExternalAccountAssociatedAttributes | AuditEventExternalAccountDisassociatedAttributes | AuditEventDomainAddedAttributes | AuditEventDomainRemovedAttributes | AuditEventDomainVerifiedAttributes | AuditEventApiAccountCreatedWithKeyAttributes | AuditEventApiAccountCreatedWithoutKeyAttributes | AuditEventApiAccountDeletedAttributes | AuditEventApiAccountKeyRevokedAttributes | AuditEventApiAccountKeyGeneratedAttributes | AuditEventApiAccountRoleLocationChangedAttributes | AuditEventApiAccountNameChangedAttributes | AuditEventRoleCreatedAttributes | AuditEventRoleUpdatedAttributes | AuditEventTermsAcceptedAttributes | AuditEventDomainFederationEnabledAttributes | AuditEventDomainFederationDisabledAttributes | AuditEventBatchPasswordResetInitiatedAttributes | AuditEventExternalAccountInvitedAttributes | AuditEventAccountImageSetAttributes | AuditEventAccountImageReplacedAttributes | AuditEventAccountImageRemovedAttributes | AuditEventIdpCreatedAttributes | AuditEventIdpUpdatedAttributes | AuditEventIdpDeletedAttributes | AuditEventIdpAccountSyncEnabledAttributes | AuditEventIdpAccountSyncDisabledAttributes | AuditEventAppleServicesSettingsUpdatedAttributes | AuditEventAccountPasswordChangedAttributes)): A polymorphic audit event resource’s attributes. Depending upon the type of event, attributes may vary.

  **Allowed Types**: `AuditEventDeviceAddedToOrgAttributes`, `AuditEventDeviceRemovedFromOrgAttributes`, `AuditEventDeviceAssignedToServerAttributes`, `AuditEventDeviceUnassignedFromServerAttributes`, `AuditEventSubjectHasIcloudStoragePurchaseAddedAttributes`, `AuditEventSubjectHasIcloudStoragePurchaseRemovedAttributes`, `AuditEventSubjectHasApplecarePurchaseAddedAttributes`, `AuditEventSubjectHasApplecarePurchaseRemovedAttributes`, `AuditEventDeviceIsErasedAttributes`, `AuditEventConfigSettingsCreatedAttributes`, `AuditEventConfigSettingsUpdatedAttributes`, `AuditEventConfigSettingsDeletedAttributes`, `AuditEventCollectionCreatedAttributes`, `AuditEventCollectionUpdatedAttributes`, `AuditEventCollectionDeletedAttributes`, `AuditEventSubscriptionCreatedAttributes`, `AuditEventSubscriptionUpdatedAttributes`, `AuditEventSubscriptionDeletedAttributes`, `AuditEventAccountRoleLocationChangedAttributes`, `AuditEventAccountAddedAttributes`, `AuditEventAccountDeletedAttributes`, `AuditEventExternalAccountAssociatedAttributes`, `AuditEventExternalAccountDisassociatedAttributes`, `AuditEventDomainAddedAttributes`, `AuditEventDomainRemovedAttributes`, `AuditEventDomainVerifiedAttributes`, `AuditEventApiAccountCreatedWithKeyAttributes`, `AuditEventApiAccountCreatedWithoutKeyAttributes`, `AuditEventApiAccountDeletedAttributes`, `AuditEventApiAccountKeyRevokedAttributes`, `AuditEventApiAccountKeyGeneratedAttributes`, `AuditEventApiAccountRoleLocationChangedAttributes`, `AuditEventApiAccountNameChangedAttributes`, `AuditEventRoleCreatedAttributes`, `AuditEventRoleUpdatedAttributes`, `AuditEventTermsAcceptedAttributes`, `AuditEventDomainFederationEnabledAttributes`, `AuditEventDomainFederationDisabledAttributes`, `AuditEventBatchPasswordResetInitiatedAttributes`, `AuditEventExternalAccountInvitedAttributes`, `AuditEventAccountImageSetAttributes`, `AuditEventAccountImageReplacedAttributes`, `AuditEventAccountImageRemovedAttributes`, `AuditEventIdpCreatedAttributes`, `AuditEventIdpUpdatedAttributes`, `AuditEventIdpDeletedAttributes`, `AuditEventIdpAccountSyncEnabledAttributes`, `AuditEventIdpAccountSyncDisabledAttributes`, `AuditEventAppleServicesSettingsUpdatedAttributes`, `AuditEventAccountPasswordChangedAttributes`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/auditevent)*