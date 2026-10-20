# AppStoreVersionExperimentV2.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an app store version experiment v2 resource.

**Availability**:
- App Store Connect API 2.4+

## Declaration

```
object AppStoreVersionExperimentV2.Attributes
```

## Properties

- `endDate` (date-time)
- `name` (string)
- `platform` (Platform)
- `reviewRequired` (boolean)
- `startDate` (date-time)
- `state` (string): **Allowed Values**: `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, `APPROVED`, `REJECTED`, `COMPLETED`, `STOPPED`
- `trafficProportion` (integer)

## See Also

### Objects
- [object AppStoreVersionExperimentV2.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionexperimentv2/attributes-data.dictionary)*