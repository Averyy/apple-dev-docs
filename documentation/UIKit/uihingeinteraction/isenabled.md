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

#### Discussion

While disabled, the interaction’s handler is not called for hinge updates, and any updates that occur are not queued. When re-enabled, the handler is called with the current hinge state if one is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihingeinteraction/isenabled)*