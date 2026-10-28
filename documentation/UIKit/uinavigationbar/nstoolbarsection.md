# UINavigationBar.NSToolbarSection

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine how the system hosts the navigation bar in an AppKit toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum NSToolbarSection
```

```c
enum UINavigationBarNSToolbarSection : NSInteger;
```

## Discussion

Not every navigation item property is supported in every toolbar section. For more information, see [Display content in a toolbar on Mac](../uinavigationitem/title.md#Display-content-in-a-toolbar-on-Mac).

## Topics

### Constants
- [UINavigationBar.NSToolbarSection.none](./nstoolbarsection/none.md)
  A constant that disables hosting the navigation bar in the toolbar.
- [UINavigationBar.NSToolbarSection.sidebar](./nstoolbarsection/sidebar.md)
  A constant that hosts the navigation bar in the toolbar’s sidebar column.
- [UINavigationBar.NSToolbarSection.supplementary](./nstoolbarsection/supplementary.md)
  A constant that hosts the navigation bar in the toolbar’s supplementary column.
- [UINavigationBar.NSToolbarSection.content](./nstoolbarsection/content.md)
  A constant that hosts the navigation bar in the toolbar’s content column.
### Initializers
- [init?(rawValue: Int)](./nstoolbarsection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Building with Mac Catalyst
- [var behavioralStyle: UIBehavioralStyle](./behavioralstyle.md)
  The behavioral style of the navigation bar.
- [var preferredBehavioralStyle: UIBehavioralStyle](./preferredbehavioralstyle.md)
  The preferred behavioral style of the navigation bar.
- [var currentNSToolbarSection: UINavigationBar.NSToolbarSection](./currentnstoolbarsection.md)
  The toolbar section that the navigation bar is currently using.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/nstoolbarsection)*