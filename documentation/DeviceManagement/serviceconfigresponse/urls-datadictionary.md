# ServiceConfigResponse.Urls

**Framework**: Device Management  
**Kind**: dictionary

The set of current service URLs.

## Declaration

```swift
object ServiceConfigResponse.Urls
```

## Mentions

- [Managing users](managing-users.md)

#### Overview

Each key names an endpoint and each value is its current URL. These URLs are dynamic and can change without notice, so sync them every 5 minutes rather than hard-coding them into your device management service.

## Properties

- `Any Key` (string)

## See Also

- [object ServiceConfigResponse.Limits](serviceconfigresponse/limits-data.dictionary.md)
  The set of current request limits.
- [object ResponseErrorCode](responseerrorcode.md)
  An error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/serviceconfigresponse/urls-data.dictionary)*