# NSItemBadge

**Framework**: AppKit  
**Kind**: struct

`NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.

**Availability**:
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct NSItemBadge
```

#### Overview

This badge provides a way to display small visual indicators, such as counts and text labels, within a toolbar item. Badges can be used to highlight important information, such as unread notifications or status indicators.

## Topics

### Instance Properties
- [var text: String](nsitembadge-swift.struct/text.md)
  The text to be displayed within the badge.
### Type Properties
- [static var indicator: NSItemBadge](nsitembadge-swift.struct/indicator.md)
  Creates a badge styled as an indicator. In this context, an indicator is simply a badge without any text.
### Type Methods
- [static func count(Int) -> NSItemBadge](nsitembadge-swift.struct/count(_:).md)
  Creates a badge displaying a localized numerical count.
- [static func text(String) -> NSItemBadge](nsitembadge-swift.struct/text(_:).md)
  Creates a badge displaying a text.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsitembadge-swift.struct)*