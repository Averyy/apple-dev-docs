# AppEventCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe an app event create request resource.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventCreateRequest.Data.Attributes
```

## Topics

### Objects
- [object AppEventCreateRequest.Data.Attributes.TerritorySchedules](appeventcreaterequest/data-data.dictionary/attributes-data.dictionary/territoryschedules-data.dictionary.md)
  The per-territory schedule attributes within an app event create request, specifying the start, end, publish dates, and targeted territories.

## Properties

- `badge` (string)
- `deepLink` (uri)
- `primaryLocale` (string)
- `priority` (string)
- `purchaseRequirement` (string)
- `purpose` (string)
- `referenceName` (string) *(required)*
- `territorySchedules` ([AppEventCreateRequest.Data.Attributes.TerritorySchedules])

## See Also

- [object AppEventCreateRequest.Data.Relationships](appeventcreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventcreaterequest/data-data.dictionary/attributes-data.dictionary)*