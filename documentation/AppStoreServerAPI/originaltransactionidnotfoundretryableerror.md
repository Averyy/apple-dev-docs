# OriginalTransactionIdNotFoundRetryableError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error response that indicates the original transaction identifier wasn’t found, but you can try again.

**Availability**:
- App Store Server API 1.0+

## Declaration

```
object OriginalTransactionIdNotFoundRetryableError
```

## Properties

- `errorCode` (int64): **Allowed Values**: `4040006`
- `errorMessage` (string): **Allowed Values**: `Original transaction id not found. Please try again.`

## See Also

### Errors to retry
- [object AccountNotFoundRetryableError](./accountnotfoundretryableerror.md)
  An error response that indicates the App Store account wasn’t found, but you can try again.
- [object AppNotFoundRetryableError](./appnotfoundretryableerror.md)
  An error response that indicates the app wasn’t found, but you can try again.
- [object GeneralInternalRetryableError](./generalinternalretryableerror.md)
  An error response that indicates an unknown error occurred, but you can try again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/originaltransactionidnotfoundretryableerror)*