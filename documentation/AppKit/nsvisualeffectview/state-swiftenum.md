# NSVisualEffectView.State

**Framework**: AppKit  
**Kind**: enum

Constants to specify how the material appearance should reflect window activity state.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum State
```

## Topics

### Visual Effect View States
- [NSVisualEffectView.State.followsWindowActiveState](nsvisualeffectview/state-swift.enum/followswindowactivestate.md)
  The backdrop should automatically appear active when the window is active, and inactive when it is not.
- [NSVisualEffectView.State.active](nsvisualeffectview/state-swift.enum/active.md)
  The backdrop should always appear active.
- [NSVisualEffectView.State.inactive](nsvisualeffectview/state-swift.enum/inactive.md)
  The backdrop should always appear inactive.
### Initializers
- [init?(rawValue: Int)](nsvisualeffectview/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: NSVisualEffectView.State](nsvisualeffectview/state-swift.property.md)
  A value that indicates whether a view has a visual effect applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/state-swift.enum)*