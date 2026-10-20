# load(handler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Type Method

Loads a broadcast activity view controller.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
class func load(handler: @escaping (RPBroadcastActivityViewController?, (any Error)?) -> Void)
```

```objc
+ (void) loadBroadcastActivityViewControllerWithHandler:(void (^)(RPBroadcastActivityViewController *broadcastActivityViewController, NSError *error)) handler;
```

#### Discussion

Present the view controller using [`present(_:animated:completion:)`](../../UIKit/uiviewcontroller/present%28_,animated,completion%29.md). Dismiss the view controller when the delegate’s [`broadcastActivityViewController(_:didFinishWith:error:)`](../rpbroadcastactivityviewcontrollerdelegate/broadcastactivityviewcontroller%28_,didfinishwith,error%29.md) method is called.

> **Note**:  On the iPad, the default presentation style for view controllers is a popover. For an instance of `RPBroadcastActivityViewController` to present properly on iPad, insure the popover presentation controller’s [`sourceRect`](../../UIKit/uipopoverpresentationcontroller/sourcerect.md) and [`sourceView`](../../UIKit/uipopoverpresentationcontroller/sourceview.md) are configured.

## Parameters

- `handler`: A block that is called after the view controller is loaded.

  - **`broadcastActivityViewController`**: The `RPBroadcastActivityViewController` to be presented.
  - **`error`**: If an error occurred, this parameter holds an object that explains the error. Otherwise, the value of this parameter is `nil`. See [`RPRecordingErrorCode`](../rprecordingerrorcode.md) for a list of error codes specific to ReplayKit.

## See Also

### Presenting the Broadcast Activity UI
- [class func load(withPreferredExtension: String?, handler: (RPBroadcastActivityViewController?, (any Error)?) -> Void)](./load%28withpreferredextension,handler%29.md)
  Loads a broadcast activity view controller with a preferred extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/load(handler:))*