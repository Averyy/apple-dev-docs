# NSVisualEffectView.State

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants to specify how the material appearance should reflect window activity state.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum State
```

```c
enum NSVisualEffectState : NSInteger;
```

## Topics

### Visual Effect View States
- [NSVisualEffectView.State.followsWindowActiveState](./state-swift.enum/followswindowactivestate.md)
  The backdrop should automatically appear active when the window is active, and inactive when it is not.
- [NSVisualEffectView.State.active](./state-swift.enum/active.md)
  The backdrop should always appear active.
- [NSVisualEffectView.State.inactive](./state-swift.enum/inactive.md)
  The backdrop should always appear inactive.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enabling or Disabling the Effect
- [var state: NSVisualEffectView.State](./state-swift.property.md)
  A value that indicates whether a view has a visual effect applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/state-swift.enum)*