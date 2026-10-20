# AppEvent.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The attributes that describe an In-App event.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
object AppEvent.Attributes
```

## Mentions

- [App Store Connect API 3.6 release notes](../app-store-connect-api-3-6-release-notes.md)

## Topics

### Objects
- [object AppEvent.Attributes.ArchivedTerritorySchedules](./attributes-data.dictionary/archivedterritoryschedules-data.dictionary.md)
  The archived per-territory schedule attributes within an app event, representing previously active territory schedules.
- [object AppEvent.Attributes.TerritorySchedules](./attributes-data.dictionary/territoryschedules-data.dictionary.md)
  The per-territory schedule attributes within an app event, defining the start, end, publish dates, and targeted territories.

## Properties

- `archivedTerritorySchedules` ([AppEvent.Attributes.ArchivedTerritorySchedules])
- `badge` (string): **Allowed Values**: `LIVE_EVENT`, `PREMIERE`, `CHALLENGE`, `COMPETITION`, `NEW_SEASON`, `MAJOR_UPDATE`, `SPECIAL_EVENT`
- `deepLink` (uri)
- `eventState` (string): **Allowed Values**: `DRAFT`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `REJECTED`, `ACCEPTED`, `APPROVED`, `PUBLISHED`, `PAST`, `ARCHIVED`
- `primaryLocale` (string)
- `priority` (string): **Allowed Values**: `HIGH`, `NORMAL`
- `purchaseRequirement` (string): Possible values: `NO_COST_ASSOCIATED`, `IN_APP_PURCHASE`
- `purpose` (string): **Allowed Values**: `APPROPRIATE_FOR_ALL_USERS`, `ATTRACT_NEW_USERS`, `KEEP_ACTIVE_USERS_INFORMED`, `BRING_BACK_LAPSED_USERS`
- `referenceName` (string)
- `territorySchedules` ([AppEvent.Attributes.TerritorySchedules])

## See Also

### Objects
- [object AppEvent.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appevent/attributes-data.dictionary)*