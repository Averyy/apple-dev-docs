# requestPermission(for:referrerURL:presenting:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Requests permission to add a blocked URL to the web content filter’s allow list.

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

## Discussion

Call this method when [`evaluateURL(_:completionHandler:)`](./evaluateurl%28_,completionhandler%29.md) or [`evaluateURL(_:mainFrameURL:isMainFrame:completionHandler:)`](./evaluateurl%28_,mainframeurl,ismainframe,completionhandler%29.md) blocks a URL and the person using your browser app asks a parent or guardian for access. The system asks the guardian to approve the request either on-device, through a pincode prompt, or remotely, through a text message to the guardian’s device. The method invokes the argument `completionHandler` to report the outcome.

## Parameters

- `url`: The blocked URL for which to request permission.
- `referrerURL`: The URL that initiates the permission request. The system uses this URL to determine whether it presents the approval request on-device or sends it remotely to a parent’s device.
- `presentingView`: The view to present the approval UI from, or `nil` if no view is available.
- `completionHandler`: A closure that the system invokes when the request completes, with a [`BEWebContentFilter.PermissionDecision`](./permissiondecision.md) that holds the outcome.

## See Also

### Requesting permission for a blocked URL
- [BEWebContentFilter.PermissionDecision](./permissiondecision.md)
  The outcome of a request to add a blocked URL to the web content filter’s allow list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter/requestpermission(for:referrerurl:presenting:completionhandler:))*