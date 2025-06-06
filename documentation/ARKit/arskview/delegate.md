# delegate

**Framework**: ARKit  
**Kind**: property

An object you provide to mediate synchronization of the view’s AR scene information with SpriteKit content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: (any ARSKViewDelegate)? { get set }
```

## See Also

- [protocol ARSKViewDelegate](arskviewdelegate.md)
  Methods you can implement to mediate the automatic synchronization of SpriteKit content with an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskview/delegate)*