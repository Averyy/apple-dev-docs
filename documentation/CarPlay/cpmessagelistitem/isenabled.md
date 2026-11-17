# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the row is enabled.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

## Discussion

When the value of this property is `true`, interactions with the row cause CarPlay to launch Siri to perform message-related tasks. When the value of this property is `false`, interactions with the row don’t trigger Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/isenabled)*