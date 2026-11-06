# RetentionMessageVersion.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a retention message version resource.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageVersion.Attributes
```

## Properties

- `state` (string): The App Review state of the retention message version. A version moves through `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED` or `REJECTED`, and then `APPROVED`. If you withdraw a version from review, its state is `DEVELOPER_REJECTED`.

  **Allowed Values**: `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `DEVELOPER_REJECTED`, `REJECTED`, `ACCEPTED`, `APPROVED`

## See Also

### Objects
- [object RetentionMessageVersion.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessageversion/attributes-data.dictionary)*