# requestPermission(for:referrerURL:presenting:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func requestPermission(for url: URL, referrerURL: URL?, presenting presentingView: UIView?) async throws -> BEWebContentFilter.PermissionDecision
```

#### Discussion

Request a blocked URL to be added to built-in web content filter’s allowlist

## Parameters

- `url`: The URL to be added.
- `referrerURL`: The URL that initiated the permission request. This determines whether or not parent approval is done remotely or on-device.
- `presentingView`: The view to present permission UI from.
- `completionHandler`: The completion block to be called when the add operation is complete, with result of the operation. Result is BEWebContentFilterPermissionDecision that holds the outcome of the request for access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/requestpermission(for:referrerurl:presenting:completionhandler:))*