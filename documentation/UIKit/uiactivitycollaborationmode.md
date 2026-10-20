# UIActivityCollaborationMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A value that defines how the system shares an item.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum UIActivityCollaborationMode
```

```c
enum UIActivityCollaborationMode : NSInteger;
```

## Topics

### Enumeration Cases
- [UIActivityCollaborationMode.collaborate](./uiactivitycollaborationmode/collaborate.md)
  The system allows collaboration on a shared item.
- [UIActivityCollaborationMode.sendCopy](./uiactivitycollaborationmode/sendcopy.md)
  The system sends a copy of the item.
### Initializers
- [init?(rawValue: Int)](./uiactivitycollaborationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Restricting the sharing mode
- [UIActivityViewController.CollaborationModeRestriction](./uiactivityviewcontroller/collaborationmoderestriction.md)
  An object that disables the sharing mode and optionally displays an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivitycollaborationmode)*