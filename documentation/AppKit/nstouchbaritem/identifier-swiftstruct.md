# NSTouchBarItem.Identifier

**Framework**: AppKit  
**Kind**: struct

An identifier for an item in the Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
struct Identifier
```

## Topics

### Creating identifiers for space items
- [static let fixedSpaceSmall: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/fixedspacesmall.md)
  The identifier of an item appropriate for use as a small space in a Touch Bar.
- [static let fixedSpaceLarge: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/fixedspacelarge.md)
  The identifier of an item appropriate for use as a large space in a Touch Bar.
- [static let flexibleSpace: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/flexiblespace.md)
  The identifier of an item appropriate for use as a flexible space in a Touch Bar.
### Creating identifiers for Touch Bar nesting
- [static let otherItemsProxy: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/otheritemsproxy.md)
  The identifier of the special “other items proxy”, which is used to nest bars up the responder chain.
### Creating identifiers for multiple choice items
- [static let candidateList: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/candidatelist.md)
  The standard identifier for a candidate list bar item.
- [static let characterPicker: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/characterpicker.md)
  The standard identifier for selecting special characters such as Emoji.
### Creating identifiers for text items
- [static let textFormat: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/textformat.md)
  The identifier for a group of text format controls.
- [static let textAlignment: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/textalignment.md)
  The identifier for a Touch Bar item used to select the text alignment.
- [static let textColorPicker: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/textcolorpicker.md)
  The identifier for a Touch Bar item used to select the text color.
- [static let textList: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/textlist.md)
  The identifier for a Touch Bar item used to control the text list style.
- [static let textStyle: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/textstyle.md)
  The identifier for a Touch Bar item used to control the text style.
### Creating a custom identifier
- [init(String)](nstouchbaritem/identifier-swift.struct/init(_:).md)
  Creates an item identifier with the specified custom name.
- [init(rawValue: String)](nstouchbaritem/identifier-swift.struct/init(rawvalue:).md)
  Creates an item identifier with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(identifier: NSTouchBarItem.Identifier)](nstouchbaritem/init(identifier:).md)
  Creates a new item with the specified identifier.
- [init?(coder: NSCoder)](nstouchbaritem/init(coder:).md)
  Initializes and returns a new item from a storyboard or nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/identifier-swift.struct)*