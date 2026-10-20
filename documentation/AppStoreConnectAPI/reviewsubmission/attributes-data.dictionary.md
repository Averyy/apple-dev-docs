# ReviewSubmission.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a review submission resource.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
object ReviewSubmission.Attributes
```

## Properties

- `platform` (Platform)
- `state` (string): **Allowed Values**: `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `UNRESOLVED_ISSUES`, `CANCELING`, `COMPLETING`, `COMPLETE`
- `submittedDate` (date-time)

## See Also

### Objects
- [object ReviewSubmission.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/reviewsubmission/attributes-data.dictionary)*