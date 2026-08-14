# UIDropSessionProgressIndicatorStyle

**Framework**: UIKit  
**Kind**: enum

The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum UIDropSessionProgressIndicatorStyle
```

## Topics

### Progress indicator styles
- [UIDropSessionProgressIndicatorStyle.default](uidropsessionprogressindicatorstyle/default.md)
  The indicator style for using the system’s default drop-progress indication.
- [UIDropSessionProgressIndicatorStyle.none](uidropsessionprogressindicatorstyle/none.md)
  The indicator style for no drop-progress indication.
### Initializers
- [init?(rawValue: UInt)](uidropsessionprogressindicatorstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol UIDropSession](uidropsession.md)
  The interface for querying a drop session about its state and associated drag items.
- [class UIDropProposal](uidropproposal.md)
  A configuration for the behavior of a drop interaction, required if a view accepts drop activities.
- [enum UIDropOperation](uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropsessionprogressindicatorstyle)*