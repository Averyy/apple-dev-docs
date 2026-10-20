# UIBarButtonItem.SystemItem

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define system-supplied images for bar button items.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum SystemItem
```

```c
enum UIBarButtonSystemItem : NSInteger;
```

## Topics

### Constants
- [UIBarButtonItem.SystemItem.done](./systemitem/done.md)
  The system Done button, localized.
- [UIBarButtonItem.SystemItem.cancel](./systemitem/cancel.md)
  The system Cancel button, localized.
- [UIBarButtonItem.SystemItem.edit](./systemitem/edit.md)
  The system Edit button, localized.
- [UIBarButtonItem.SystemItem.save](./systemitem/save.md)
  The system Save button, localized.
- [UIBarButtonItem.SystemItem.add](./systemitem/add.md)
  The system plus button containing an icon of a plus sign.
- [UIBarButtonItem.SystemItem.flexibleSpace](./systemitem/flexiblespace.md)
  Blank space to add between other items.
- [UIBarButtonItem.SystemItem.fixedSpace](./systemitem/fixedspace.md)
  Blank space to add between other items.
- [UIBarButtonItem.SystemItem.compose](./systemitem/compose.md)
  The system compose button.
- [UIBarButtonItem.SystemItem.reply](./systemitem/reply.md)
  The system reply button.
- [UIBarButtonItem.SystemItem.action](./systemitem/action.md)
  The system action button.
- [UIBarButtonItem.SystemItem.organize](./systemitem/organize.md)
  The system organize button.
- [UIBarButtonItem.SystemItem.bookmarks](./systemitem/bookmarks.md)
  The system bookmarks button.
- [UIBarButtonItem.SystemItem.search](./systemitem/search.md)
  The system search button.
- [UIBarButtonItem.SystemItem.refresh](./systemitem/refresh.md)
  The system refresh button.
- [UIBarButtonItem.SystemItem.stop](./systemitem/stop.md)
  The system stop button.
- [UIBarButtonItem.SystemItem.camera](./systemitem/camera.md)
  The system camera button.
- [UIBarButtonItem.SystemItem.trash](./systemitem/trash.md)
  The system trash button.
- [UIBarButtonItem.SystemItem.play](./systemitem/play.md)
  The system play button.
- [UIBarButtonItem.SystemItem.pause](./systemitem/pause.md)
  The system pause button.
- [UIBarButtonItem.SystemItem.rewind](./systemitem/rewind.md)
  The system rewind button.
- [UIBarButtonItem.SystemItem.fastForward](./systemitem/fastforward.md)
  The system fast forward button.
- [UIBarButtonItem.SystemItem.undo](./systemitem/undo.md)
  The system undo button.
- [UIBarButtonItem.SystemItem.redo](./systemitem/redo.md)
  The system redo button.
- [UIBarButtonItem.SystemItem.close](./systemitem/close.md)
  The system close button.
- [UIBarButtonItem.SystemItem.writingTools](./systemitem/writingtools.md)
- [UIBarButtonItem.SystemItem.pageCurl](./systemitem/pagecurl.md)
  The system page curl button.
### Initializers
- [init?(rawValue: Int)](./systemitem/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating system items
- [convenience init(systemItem: UIBarButtonItem.SystemItem, primaryAction: UIAction?, menu: UIMenu?)](./init%28systemitem,primaryaction,menu%29.md)
  Creates an item using the specified system item, primary action, and context menu.
- [convenience init(barButtonSystemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)](./init%28barbuttonsystemitem,target,action%29.md)
  Creates an item using the specified system item, target, and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/systemitem)*