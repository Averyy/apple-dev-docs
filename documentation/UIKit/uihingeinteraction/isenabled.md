# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Whether the interaction is enabled.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Discussion

When the interaction is disabled, if the handler’s last update had a hinge, the handler is called once more with a nil `hinge`. After that, the handler isn’t called for hinge updates, and updates that occur while the interaction is disabled aren’t queued. When the interaction is re-enabled, the handler is called with the current hinge state if one is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihingeinteraction/isenabled)*