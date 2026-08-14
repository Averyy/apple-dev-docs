# ServiceConfigResponse.Limits

**Framework**: Device Management  
**Kind**: dictionary

The set of current request limits.

## Declaration

```swift
object ServiceConfigResponse.Limits
```

## Mentions

- [Managing assets](managing-assets.md)
- [Managing subscriptions](managing-subscriptions.md)
- [Managing users](managing-users.md)

#### Overview

Each key names a limit and each value is the current limit. The set of keys varies by endpoint, and the limits are dynamic and can change without notice, so sync them every 5 minutes.

## Properties

- `Any Key` (int32)

## See Also

- [object ServiceConfigResponse.Urls](serviceconfigresponse/urls-data.dictionary.md)
  The set of current service URLs.
- [object ResponseErrorCode](responseerrorcode.md)
  An error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/serviceconfigresponse/limits-data.dictionary)*