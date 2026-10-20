# NSTabViewItem.State

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants describe the current display state of a tab:

**Availability**:
- macOS

## Declaration

```swift
enum State
```

```c
enum NSTabState : NSUInteger;
```

## Topics

### Constants
- [NSTabViewItem.State.backgroundTab](./state/backgroundtab.md)
  A tab that’s not being displayed.
- [NSTabViewItem.State.pressedTab](./state/pressedtab.md)
  A tab that the user is in the process of clicking. That is, the user has pressed the mouse button while the cursor is over the tab but has not released the mouse button.
- [NSTabViewItem.State.selectedTab](./state/selectedtab.md)
  The tab that’s being displayed.
### Initializers
- [init?(rawValue: UInt)](./state/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/state)*