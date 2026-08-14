# ServiceConfigResponse

**Framework**: Device Management  
**Kind**: dictionary

The service configuration for the Asset Management API.

## Declaration

```swift
object ServiceConfigResponse
```

#### Discussion

The values in `limits` and `urls` are dynamic and can change without notice. Sync them every 5 minutes rather than hard-coding them into your device management service.

## Topics

### Objects and Data Types
- [object ServiceConfigResponse.Limits](serviceconfigresponse/limits-data.dictionary.md)
  The set of current request limits.
- [object ServiceConfigResponse.Urls](serviceconfigresponse/urls-data.dictionary.md)
  The set of current service URLs.
- [object ResponseErrorCode](responseerrorcode.md)
  An error code.

## Properties

- `errorCodes` ([ResponseErrorCode]): The set of possible error numbers and their human-readable explanations.
- `limits` (ServiceConfigResponse.Limits): The set of current request limits.
- `notificationTypes` ([string]): The set of supported notification types.
- `urls` (ServiceConfigResponse.Urls): The set of current service URLs.

## See Also

- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/serviceconfigresponse)*