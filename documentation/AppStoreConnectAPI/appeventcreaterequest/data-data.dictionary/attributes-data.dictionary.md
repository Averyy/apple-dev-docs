# AppEventCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an app event create request resource.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
object AppEventCreateRequest.Data.Attributes
```

## Topics

### Objects
- [object AppEventCreateRequest.Data.Attributes.TerritorySchedules](./attributes-data.dictionary/territoryschedules-data.dictionary.md)
  The per-territory schedule attributes within an app event create request, specifying the start, end, publish dates, and targeted territories.

## Properties

- `badge` (string): **Allowed Values**: `LIVE_EVENT`, `PREMIERE`, `CHALLENGE`, `COMPETITION`, `NEW_SEASON`, `MAJOR_UPDATE`, `SPECIAL_EVENT`
- `deepLink` (uri)
- `primaryLocale` (string)
- `priority` (string): **Allowed Values**: `HIGH`, `NORMAL`
- `purchaseRequirement` (string)
- `purpose` (string): **Allowed Values**: `APPROPRIATE_FOR_ALL_USERS`, `ATTRACT_NEW_USERS`, `KEEP_ACTIVE_USERS_INFORMED`, `BRING_BACK_LAPSED_USERS`
- `referenceName` (string) *(required)*
- `territorySchedules` ([AppEventCreateRequest.Data.Attributes.TerritorySchedules])

## See Also

### Objects
- [object AppEventCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventcreaterequest/data-data.dictionary/attributes-data.dictionary)*