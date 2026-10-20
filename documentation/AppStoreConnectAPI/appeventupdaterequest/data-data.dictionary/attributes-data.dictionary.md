# AppEventUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an app event update request resource.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
object AppEventUpdateRequest.Data.Attributes
```

## Topics

### Objects
- [object AppEventUpdateRequest.Data.Attributes.TerritorySchedules](./attributes-data.dictionary/territoryschedules-data.dictionary.md)
  The per-territory schedule attributes within an app event update request, specifying the start, end, publish dates, and targeted territories.

## Properties

- `badge` (string): **Allowed Values**: `LIVE_EVENT`, `PREMIERE`, `CHALLENGE`, `COMPETITION`, `NEW_SEASON`, `MAJOR_UPDATE`, `SPECIAL_EVENT`
- `deepLink` (uri)
- `primaryLocale` (string)
- `priority` (string): **Allowed Values**: `HIGH`, `NORMAL`
- `purchaseRequirement` (string)
- `purpose` (string): **Allowed Values**: `APPROPRIATE_FOR_ALL_USERS`, `ATTRACT_NEW_USERS`, `KEEP_ACTIVE_USERS_INFORMED`, `BRING_BACK_LAPSED_USERS`
- `referenceName` (string)
- `territorySchedules` ([AppEventUpdateRequest.Data.Attributes.TerritorySchedules])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventupdaterequest/data-data.dictionary/attributes-data.dictionary)*