# delegate

**Framework**: ARKit  
**Kind**: property

An object you provide to mediate synchronization of the view’s AR scene information with SceneKit content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
weak var delegate: (any ARSCNViewDelegate)? { get set }
```

## See Also

- [protocol ARSCNViewDelegate](arscnviewdelegate.md)
  Methods you can implement to mediate the automatic synchronization of SceneKit content with an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/delegate)*