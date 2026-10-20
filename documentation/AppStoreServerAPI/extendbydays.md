# extendByDays

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The number of days to extend the subscription renewal date.

**Availability**:
- App Store Server API 1.1+

## Declaration

```
int32 extendByDays
```



**Maximum**: `90`

**Minimum**: `1`

#### Discussion

The number of days is a number from 1 to 90.

## See Also

### Request data types
- [type extendReasonCode](./extendreasoncode.md)
  The code that represents the reason for the subscription-renewal-date extension.
- [type requestIdentifier](./requestidentifier.md)
  A string that contains a unique identifier you provide to track each subscription-renewal-date extension request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/extendbydays)*