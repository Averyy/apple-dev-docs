# extendReasonCode

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The code that represents the reason for the subscription-renewal-date extension.

**Availability**:
- App Store Server API 1.1+

## Declaration

```
int32 extendReasonCode
```

## Possible Values

- `0`: Undeclared; no information provided.
- `1`: The renewal-date extension is for customer satisfaction.
- `2`: The renewal-date extension is for other reasons.
- `3`: The renewal-date extension is due to a service issue or outage.

#### Discussion

For more information about requesting subscription-renewal-date extensions, see [Extending the renewal date for auto-renewable subscriptions](./extending-the-renewal-date-for-auto-renewable-subscriptions.md).

## See Also

### Request data types
- [type extendByDays](./extendbydays.md)
  The number of days to extend the subscription renewal date.
- [type requestIdentifier](./requestidentifier.md)
  A string that contains a unique identifier you provide to track each subscription-renewal-date extension request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/extendreasoncode)*