# AuditEventType

**Framework**: AppleBusinessAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent audit event types.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
string AuditEventType
```

## Possible Values

- `DEVICE_ADDED_TO_ORG`
- `DEVICE_REMOVED_FROM_ORG`
- `DEVICE_ASSIGNED_TO_SERVER`
- `DEVICE_UNASSIGNED_FROM_SERVER`
- `SUBJECT_HAS_ICLOUD_STORAGE_PURCHASE_ADDED`
- `SUBJECT_HAS_ICLOUD_STORAGE_PURCHASE_REMOVED`
- `SUBJECT_HAS_APPLECARE_PURCHASE_ADDED`
- `SUBJECT_HAS_APPLECARE_PURCHASE_REMOVED`
- `DEVICE_IS_ERASED`
- `CONFIG_SETTINGS_CREATED`
- `CONFIG_SETTINGS_UPDATED`
- `CONFIG_SETTINGS_DELETED`
- `COLLECTION_CREATED`
- `COLLECTION_UPDATED`
- `COLLECTION_DELETED`
- `SUBSCRIPTION_CREATED`
- `SUBSCRIPTION_UPDATED`
- `SUBSCRIPTION_DELETED`
- `ACCOUNT_ROLE_LOCATION_CHANGED`
- `ACCOUNT_ADDED`
- `ACCOUNT_DELETED`
- `EXTERNAL_ACCOUNT_ASSOCIATED`
- `EXTERNAL_ACCOUNT_DISASSOCIATED`
- `DOMAIN_ADDED`
- `DOMAIN_REMOVED`
- `DOMAIN_VERIFIED`
- `API_ACCOUNT_CREATED_WITH_KEY`
- `API_ACCOUNT_CREATED_WITHOUT_KEY`
- `API_ACCOUNT_DELETED`
- `API_ACCOUNT_KEY_REVOKED`
- `API_ACCOUNT_KEY_GENERATED`
- `API_ACCOUNT_ROLE_LOCATION_CHANGED`
- `API_ACCOUNT_NAME_CHANGED`
- `ROLE_CREATED`
- `ROLE_UPDATED`
- `TERMS_ACCEPTED`
- `DOMAIN_FEDERATION_ENABLED`
- `DOMAIN_FEDERATION_DISABLED`
- `BATCH_PASSWORD_RESET_INITIATED`
- `EXTERNAL_ACCOUNT_INVITED`
- `ACCOUNT_IMAGE_SET`
- `ACCOUNT_IMAGE_REPLACED`
- `ACCOUNT_IMAGE_REMOVED`
- `IDP_CREATED`
- `IDP_UPDATED`
- `IDP_DELETED`
- `IDP_ACCOUNT_SYNC_ENABLED`
- `IDP_ACCOUNT_SYNC_DISABLED`
- `APPLE_SERVICES_SETTINGS_UPDATED`
- `ACCOUNT_PASSWORD_CHANGED`

## Discussion

- Possible Values

  - DEVICE_ADDED_TO_ORG: Device added to organization.
  - DEVICE_REMOVED_FROM_ORG: Device removed from organization.
  - DEVICE_ASSIGNED_TO_SERVER: Device assigned to a device management service.
  - DEVICE_UNASSIGNED_FROM_SERVER: Device unassigned from a device management service.
  - SUBJECT_HAS_ICLOUD_STORAGE_PURCHASE_ADDED: iCloud storage purchase added.
  - SUBJECT_HAS_ICLOUD_STORAGE_PURCHASE_REMOVED: iCloud storage purchase removed.
  - SUBJECT_HAS_APPLECARE_PURCHASE_ADDED: AppleCare purchase added.
  - SUBJECT_HAS_APPLECARE_PURCHASE_REMOVED: AppleCare purchase removed.
  - DEVICE_IS_ERASED: Device is erased.
  - CONFIG_SETTINGS_CREATED: Configuration settings created.
  - CONFIG_SETTINGS_UPDATED: Configuration settings updated.
  - CONFIG_SETTINGS_DELETED: Configuration settings deleted.
  - COLLECTION_CREATED: Collection created.
  - COLLECTION_UPDATED: Collection updated.
  - COLLECTION_DELETED: Collection deleted.
  - SUBSCRIPTION_CREATED: Subscription created.
  - SUBSCRIPTION_UPDATED: Subscription updated.
  - SUBSCRIPTION_DELETED: Subscription deleted.
  - ACCOUNT_ROLE_LOCATION_CHANGED: User’s role@location changed.
  - ACCOUNT_ADDED: Account added.
  - ACCOUNT_DELETED: Account deleted.
  - EXTERNAL_ACCOUNT_ASSOCIATED: External account associated.
  - EXTERNAL_ACCOUNT_DISASSOCIATED: External account disassociated.
  - DOMAIN_ADDED: Domain added to organization.
  - DOMAIN_REMOVED: Domain removed from organization.
  - DOMAIN_VERIFIED: Domain verified.
  - API_ACCOUNT_CREATED_WITH_KEY: API account created with associated key.
  - API_ACCOUNT_CREATED_WITHOUT_KEY: API account created without a key.
  - API_ACCOUNT_DELETED: API account deleted.
  - API_ACCOUNT_KEY_REVOKED: Key associated with API account is revoked.
  - API_ACCOUNT_KEY_GENERATED: Key generated for API account.
  - API_ACCOUNT_ROLE_LOCATION_CHANGED: API account’s role@location changed.
  - API_ACCOUNT_NAME_CHANGED: API account name changed.
  - ROLE_CREATED: Role created.
  - ROLE_UPDATED: Role updated.
  - TERMS_ACCEPTED: Terms and conditions accepted.
  - DOMAIN_FEDERATION_ENABLED: Domain federation enabled.
  - DOMAIN_FEDERATION_DISABLED: Domain federation disabled.
  - BATCH_PASSWORD_RESET_INITIATED: Batch password reset initiated.
  - EXTERNAL_ACCOUNT_INVITED: External account invited.
  - ACCOUNT_IMAGE_SET: Account image set.
  - ACCOUNT_IMAGE_REPLACED: Account image replaced.
  - ACCOUNT_IMAGE_REMOVED: Account image removed.
  - IDP_CREATED: Identity provider created.
  - IDP_UPDATED: Identity provider updated.
  - IDP_DELETED: Identity provider deleted.
  - IDP_ACCOUNT_SYNC_ENABLED: Identity provider account sync enabled.
  - IDP_ACCOUNT_SYNC_DISABLED: Identity provider account sync disabled.
  - APPLE_SERVICES_SETTINGS_UPDATED: Apple services settings updated.
  - ACCOUNT_PASSWORD_CHANGED: Account password changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/auditeventtype)*