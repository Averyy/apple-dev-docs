# ErrorResponse

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary

Information about errors that the API returns in the response body whenever an API request is unsuccessful.

**Availability**:
- App Store Connect API 1.0.10+
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```swift
object ErrorResponse
```

## Properties

- `errorMessage` (string) *(required)*: A description of the error.
- `statusCode` (integer) *(required)*: The HTTP status code.
- `subStatusCode` (integer) *(required)*: A specific sub-status code the system provides to give more context on the type of error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/errorresponse)*