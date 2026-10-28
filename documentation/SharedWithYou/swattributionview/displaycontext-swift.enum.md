# SWAttributionView.DisplayContext

**Framework**: Shared with You  
**Kind**: enum  
**Role**: Enumeration

The context for the content that influences the ranking of this view’s highlight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum DisplayContext
```

```c
enum SWAttributionViewDisplayContext : NSInteger;
```

## Mentions

- [Making your app content shareable](../making-your-app-content-shareable.md)

## Overview

Set the appropriate display context on [`SWAttributionView`](../swattributionview.md) before the system adds the view to a window. This informs the system about how the user is consuming the attributed content, and influences future relevancy ranking of the [`SWHighlight`](../swhighlight.md) for this view.

## Topics

### Context styles
- [SWAttributionView.DisplayContext.summary](./displaycontext-swift.enum/summary.md)
  Indicates that the system is offering the attributed content shown along with this view to the user for consumption.
- [SWAttributionView.DisplayContext.detail](./displaycontext-swift.enum/detail.md)
  Indicates that the attributed content shown along with this view is being actively consumed by the user.
### Initializers
- [init?(rawValue: Int)](./displaycontext-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing the view
- [SWAttributionView.BackgroundStyle](./backgroundstyle-swift.enum.md)
  The background styling of the attribution view’s contents.
- [SWAttributionView.HorizontalAlignment](./horizontalalignment-swift.enum.md)
  The horizontal alignment of attribution view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swattributionview/displaycontext-swift.enum)*