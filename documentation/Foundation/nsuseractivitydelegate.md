# NSUserActivityDelegate

**Framework**: Foundation  
**Kind**: protocol

The interface through which a user activity instance notifies its delegate of updates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol NSUserActivityDelegate : NSObjectProtocol
```

#### Overview

An object conforming to the [`NSUserActivityDelegate`](nsuseractivitydelegate.md) protocol works with an [`NSUserActivity`](nsuseractivity.md) object, which encapsulates the state of a user activity in an application on a particular device and enables the same activity to be continued on another device. For example, a user browsing an article in Safari on a Mac can move to an iOS device where the same webpage automatically opens in Safari with the same scroll position.

The user activity delegate is responsible for updating the state of an activity and is also notified when an activity has been continued on another device. The user activity delegate is typically a top-level object in the app—such as a window, view controller, or the app delegate—that manages the activity’s interaction with the app.

## Topics

### Handling streams
- [func userActivity(NSUserActivity, didReceive: InputStream, outputStream: OutputStream)](nsuseractivitydelegate/useractivity(_:didreceive:outputstream:).md)
  Notifies the user activity delegate that an input and output streams are available to open.
### Managing activity continuation
- [func userActivityWasContinued(NSUserActivity)](nsuseractivitydelegate/useractivitywascontinued(_:).md)
  Notifies the delegate that the user activity was continued on another device.
- [func userActivityWillSave(NSUserActivity)](nsuseractivitydelegate/useractivitywillsave(_:).md)
  Notifies the delegate that the user activity will be saved to be continued or persisted.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSUserActivity](nsuseractivity.md)
  A representation of the state of your app at a moment in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivitydelegate)*