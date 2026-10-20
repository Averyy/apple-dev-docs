# error

**Framework**: App Store Receipts  
**Kind**: dictionary  
**Role**: Object

Error information that returns in the response body when a request isn’t successful.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

## Declaration

```
object error
```

## Properties

- `code` (int32) *(required)* *(deprecated)*: A standard HTTP status code returned in the response body whenever a request isn’t successful due to a general networking issue.

## See Also

### Deprecated
- [verifyReceipt](./verify-receipt.md)
  Send a receipt to the App Store for verification.
- [object requestBody](./requestbody.md)
  The JSON contents you submit with the request to the App Store.
- [object responseBody](./responsebody.md)
  The JSON data that returns in the response from the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/error)*