# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that configures and controls a drop interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIDropInteractionDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UIDropInteractionDelegate> delegate;
```

## See Also

### Managing drop interactions
- [protocol UIDropInteractionDelegate](../uidropinteractiondelegate.md)
  The interface for configuring and controlling a drop interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteraction/delegate)*