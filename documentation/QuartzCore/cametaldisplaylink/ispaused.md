# isPaused

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system suspends the display link’s notifications to the target.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isPaused: Bool { get set }
```

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

## Discussion

You can instruct the display link to stop sending notifications to the delegate by setting the property to [`true`](../../Swift/true.md). The property defaults to [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/ispaused)*