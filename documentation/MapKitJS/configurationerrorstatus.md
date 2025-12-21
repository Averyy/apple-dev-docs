# ConfigurationErrorStatus

**Framework**: MapKit JS  
**Kind**: enum

A value that represents the status of a configuration error.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const ConfigurationErrorStatus: Readonly<{
    readonly BadRequest: "Bad Request";
    readonly Unauthorized: "Unauthorized";
    readonly TooManyRequests: "Too Many Requests";
    readonly MalformedResponse: "Malformed Response";
    readonly Timeout: "Timeout";
    readonly NetworkError: "Network Error";
    readonly Unknown: "Unknown";
}>
```

## Topics

### Enumeration Cases
- [BadRequest](configurationerrorstatus/badrequest.md)
  An error status value that indicates the service returned a bad request response when initializing.
- [MalformedResponse](configurationerrorstatus/malformedresponse.md)
  An error status that indicates the service returned a malformed response when initializing.
- [NetworkError](configurationerrorstatus/networkerror.md)
  An error status that indicates MapKit JS encountered a network error during initialization.
- [Timeout](configurationerrorstatus/timeout.md)
  An error status that indicates the service timed out when initializing.
- [TooManyRequests](configurationerrorstatus/toomanyrequests.md)
  An error status that indicates the Maps ID for the authorization token provided exceeded its allowed daily usage.
- [Unauthorized](configurationerrorstatus/unauthorized.md)
  An error status that indicates the provided authorization token is invalid.
- [Unknown](configurationerrorstatus/unknown.md)
  An error status that indicates MapKit JS encountered an unknown error during initialization.
### Type Aliases
- [type ConfigurationErrorStatus](configurationerrorstatus/configurationerrorstatus.md)
  A type alias that represents the values of the configuration error status enumeration.

## See Also

- [const ConfigurationChangeStatus](configurationchangestatus.md)
  Values that represent the status of a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/configurationerrorstatus)*