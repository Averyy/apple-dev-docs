# requestPermission(for:referrerURL:presenting:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
func requestPermission(for url: URL, referrerURL: URL?, presenting presentingView: UIView?, completionHandler: @escaping @Sendable (BEWebContentFilter.PermissionDecision, (any Error)?) -> Void)
```

```swift
func requestPermission(for url: URL, referrerURL: URL?, presenting presentingView: UIView?) async throws -> BEWebContentFilter.PermissionDecision
```

```objc
- (void) requestPermissionForURL:(NSURL *) url referrerURL:(NSURL *) referrerURL presentingView:(UIView *) presentingView completionHandler:(void (^)(BEWebContentFilterPermissionDecision result, NSError *error)) completionHandler;
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