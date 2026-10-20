# suspensionReasons

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The reasons a coordinator is currently unable to participate in a group playback activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * suspensionReasons;
```

#### Discussion

The coordinator doesn’t respond to changes in group playback state when this property value contains suspension reasons.

> **Note**:  To observe changes to this property value, register for notifications of type [`suspensionReasonsDidChangeNotification`](./suspensionreasonsdidchangenotification.md).

## See Also

### Observing suspension reasons
- [class let suspensionReasonsDidChangeNotification: NSNotification.Name](./suspensionreasonsdidchangenotification.md)
  A notification that the coordinator posts when its suspension reasons change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/suspensionreasons)*