# load(withPreferredExtension:handler:)

**Framework**: ReplayKit  
**Kind**: method

Loads a broadcast activity view controller with a preferred extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func load(withPreferredExtension preferredExtension: String?, handler: @escaping (RPBroadcastActivityViewController?, (any Error)?) -> Void)
```

#### Discussion

Present the view controller using [`present(_:animated:completion:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/present(_:animated:completion:)). Dismiss the view controller when the delegate’s [`broadcastActivityViewController(_:didFinishWith:error:)`](rpbroadcastactivityviewcontrollerdelegate/broadcastactivityviewcontroller(_:didfinishwith:error:).md) method is called.

> **Note**:  On the iPad, the default presentation style for view controllers is a popover. For an instance of `RPBroadcastActivityViewController` to present properly on iPad, insure the popover presentation controller’s [`sourceRect`](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourcerect) and [`sourceView`](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/sourceview) are configured.

## Parameters

- `preferredExtension`: The extension bundle identifier for the preferred broadcast extension service.
- `handler`: A block that is called after the view controller is loaded. - **broadcastActivityViewController**: The `RPBroadcastActivityViewController` to be presented.
- **error**: If an error occurred, this parameter holds an object that explains the error. Otherwise, the value of this parameter is `nil`. See [`RPRecordingErrorCode`](rprecordingerrorcode.md) for a list of error codes specific to ReplayKit.

## See Also

- [class func load(handler: (RPBroadcastActivityViewController?, (any Error)?) -> Void)](rpbroadcastactivityviewcontroller/load(handler:).md)
  Loads a broadcast activity view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/load(withpreferredextension:handler:))*