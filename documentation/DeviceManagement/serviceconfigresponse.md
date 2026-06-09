# ServiceConfigResponse

**Framework**: Device Management  
**Kind**: dictionary

Service configuration, including request limits, available URLs, supported notification types, and error code reference information.

## Declaration

```swift
object ServiceConfigResponse
```

## Topics

### Dictionaries
- [object ServiceConfigResponse.Limits](serviceconfigresponse/limits-data.dictionary.md)
  Request limits for the managed location. Each entry maps a limit name to its current integer value.
- [object ServiceConfigResponse.Urls](serviceconfigresponse/urls-data.dictionary.md)
  Service URLs for the managed location. Each entry maps a URL name to its corresponding endpoint.

## Properties

- `errorCodes` ([ResponseErrorCode])
- `limits` (ServiceConfigResponse.Limits)
- `notificationTypes` ([string])
- `urls` (ServiceConfigResponse.Urls)

## See Also

- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/serviceconfigresponse)*