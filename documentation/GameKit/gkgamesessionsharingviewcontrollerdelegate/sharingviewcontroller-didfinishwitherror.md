# sharingViewController(_:didFinishWithError:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Indicates the sharing view controller is ready to be dismissed.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
func sharingViewController(_ viewController: GKGameSessionSharingViewController, didFinishWithError error: (any Error)?)
```

## Parameters

- `viewController`: The sharing view controller to be dismissed.
- `error`: An optional GameKit error. This parameter is   if the sharing view controller is successfully dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontrollerdelegate/sharingviewcontroller(_:didfinishwitherror:))*