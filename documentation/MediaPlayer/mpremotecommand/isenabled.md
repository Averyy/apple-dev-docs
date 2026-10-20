# isEnabled

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a user can interact with the displayed element.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the designated element is enabled so users can interact with it. When set to [`false`](../../Swift/false.md), events for this command are not sent to your app, and the user interface may be changed to reflect this when your app is the Now Playing app. The default value is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/isenabled)*