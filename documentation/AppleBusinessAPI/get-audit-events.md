# Get Audit Events

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of audit events in an organization that satisfies the query criteria.

**Availability**:
- Apple Business API 2.6+

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/auditEvents?filter[startTimestamp]=2026-03-01T00:00:00Z&filter[endTimestamp]=2025-03-02T23:59:59Z&limit=100" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
    {
    "data": [
        {
            "type": "auditEvents",
            "id": "event-12345",
            "attributes": {
                "eventDateTime": "2026-02-14T12:00:00Z",
                "type": "DEVICE_ADDED_TO_ORG",
                "category": "DEVICE_INVENTORY",
                "actorType": "USER",
                "actorId": "user-abc123",
                "actorName": "elana.landot@melardclothing.com",
                "subjectType": "DEVICE",
                "subjectId": "device-xyz789",
                "subjectName": "MacBook Pro",
                "outcome": "SUCCESS",
                "groupId": "group-001",
                "eventDataPropertyKey": "eventDataDeviceAddedToOrg",
                "eventDataDeviceAddedToOrg": {
                    "serialNumber": "C02X1234ABCD",
                    "purchaseSourceType": "APPLE",
                    "purchaseSourceId": "order-56789"
                    }
                }
            }
        ],
    "links": {
        "self": "<llink to query to generate this output>"
        "next": "<llink to next page of data, if more data is available>"
        },  
    "meta": {
        "paging": {
            "nextCursor": "next-page-token"
            "limit": 5
        }  
    }
}
```

## Topics

### Responses
- [object AuditEventsResponse](./auditeventsresponse.md)
  The response containing a list of audit events.

## Endpoint

`GET https://api-business.apple.com/v1/auditEvents`

## Parameters

### Query Parameters

- `filter[startTimestamp]` ([string]) *(required)*: ISO8601 formatted start timestamp of query time range.
- `filter[endTimestamp]` ([string]) *(required)*: ISO8601 formatted end timestamp of query time range.
- `filter[actorId]` ([string]): Id of actor of event. Note that only one actor id in query is supported.
- `filter[subjectId]` ([string]): Id of subject of event. Note that only one subject id in query is supported.
- `filter[type]` ([string]): Type of event. Note that only one type in query is supported.

  **Allowed Values**: `DEVICE_ADDED_TO_ORG`, `DEVICE_REMOVED_FROM_ORG`, `DEVICE_ASSIGNED_TO_SERVER`, `DEVICE_UNASSIGNED_FROM_SERVER`, `SUBJECT_HAS_ICLOUD_STORAGE_PURCHASE_ADDED`, `SUBJECT_HAS_ICLOUD_STORAGE_PURCHASE_REMOVED`, `SUBJECT_HAS_APPLECARE_PURCHASE_ADDED`, `SUBJECT_HAS_APPLECARE_PURCHASE_REMOVED`, `DEVICE_IS_ERASED`, `CONFIG_SETTINGS_CREATED`, `CONFIG_SETTINGS_UPDATED`, `CONFIG_SETTINGS_DELETED`, `COLLECTION_CREATED`, `COLLECTION_UPDATED`, `COLLECTION_DELETED`, `SUBSCRIPTION_CREATED`, `SUBSCRIPTION_UPDATED`, `SUBSCRIPTION_DELETED`, `ACCOUNT_ROLE_LOCATION_CHANGED`, `ACCOUNT_ADDED`, `ACCOUNT_DELETED`, `EXTERNAL_ACCOUNT_ASSOCIATED`, `EXTERNAL_ACCOUNT_DISASSOCIATED`, `DOMAIN_ADDED`, `DOMAIN_REMOVED`, `DOMAIN_VERIFIED`, `API_ACCOUNT_CREATED_WITH_KEY`, `API_ACCOUNT_CREATED_WITHOUT_KEY`, `API_ACCOUNT_DELETED`, `API_ACCOUNT_KEY_REVOKED`, `API_ACCOUNT_KEY_GENERATED`, `API_ACCOUNT_ROLE_LOCATION_CHANGED`, `API_ACCOUNT_NAME_CHANGED`, `ROLE_CREATED`, `ROLE_UPDATED`, `TERMS_ACCEPTED`, `DOMAIN_FEDERATION_ENABLED`, `DOMAIN_FEDERATION_DISABLED`, `BATCH_PASSWORD_RESET_INITIATED`, `EXTERNAL_ACCOUNT_INVITED`, `ACCOUNT_IMAGE_SET`, `ACCOUNT_IMAGE_REPLACED`, `ACCOUNT_IMAGE_REMOVED`, `IDP_CREATED`, `IDP_UPDATED`, `IDP_DELETED`, `IDP_ACCOUNT_SYNC_ENABLED`, `IDP_ACCOUNT_SYNC_DISABLED`, `APPLE_SERVICES_SETTINGS_UPDATED`, `ACCOUNT_PASSWORD_CHANGED`
- `limit` (integer): The number of included related resources to return.

  **Maximum**: `1000`
- `fields[auditEvents]` ([string]): **Allowed Values**: `eventDateTime`, `type`, `category`, `actorType`, `actorId`, `actorName`, `subjectType`, `subjectId`, `subjectName`, `outcome`, `groupId`, `eventDataPropertyKey`, `eventDataDeviceAddedToOrg`, `eventDataDeviceRemovedFromOrg`, `eventDataDeviceAssignedToServer`, `eventDataDeviceIsErased`, `eventDataDeviceUnassignedFromServer`, `eventDataSubjectHasICloudStoragePurchaseAdded`, `eventDataSubjectHasICloudStoragePurchaseRemoved`, `eventDataSubjectHasAppleCarePurchaseAdded`, `eventDataSubjectHasAppleCarePurchaseRemoved`, `eventDataConfigSettingsCreated`, `eventDataConfigSettingsUpdated`, `eventDataConfigSettingsDeleted`, `eventDataCollectionCreated`, `eventDataCollectionUpdated`, `eventDataCollectionDeleted`, `eventDataSubscriptionCreated`, `eventDataSubscriptionUpdated`, `eventDataSubscriptionDeleted`, `eventDataAccountRoleLocationChanged`, `eventDataAccountAdded`, `eventDataAccountDeleted`, `eventDataExternalAccountAssociated`, `eventDataExternalAccountDisassociated`, `eventDataDomainAdded`, `eventDataDomainRemoved`, `eventDataDomainVerified`, `eventDataApiAccountCreatedWithKey`, `eventDataApiAccountCreatedWithoutKey`, `eventDataApiAccountDeleted`, `eventDataApiAccountKeyGenerated`, `eventDataApiAccountKeyRevoked`, `eventDataApiAccountNameChanged`, `eventDataApiAccountRoleLocationChanged`, `eventDataRoleCreated`, `eventDataRoleUpdated`, `eventDataTermsAccepted`, `eventDataDomainFederationEnabled`, `eventDataDomainFederationDisabled`, `eventDataBatchPasswordResetInitiated`, `eventDataExternalAccountInvited`, `eventDataAccountImageSet`, `eventDataAccountImageReplaced`, `eventDataAccountImageRemoved`, `eventDataIdpCreated`, `eventDataIdpUpdated`, `eventDataIdpDeleted`, `eventDataIdpAccountSyncEnabled`, `eventDataIdpAccountSyncDisabled`, `eventDataAppleServicesSettingsUpdated`, `eventDataAccountPasswordChanged`
- `cursor` (string)

## Responses

- `200` OK (`AuditEventsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-audit-events)*