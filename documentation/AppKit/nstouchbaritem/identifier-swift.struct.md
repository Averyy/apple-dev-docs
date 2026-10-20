# NSTouchBarItem.Identifier

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

An identifier for an item in the Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
struct Identifier
```

```c
typedef NSString * NSTouchBarItemIdentifier;
```

## Topics

### Creating identifiers for space items
- [static let fixedSpaceSmall: NSTouchBarItem.Identifier](./identifier-swift.struct/fixedspacesmall.md)
  The identifier of an item appropriate for use as a small space in a Touch Bar.
- [static let fixedSpaceLarge: NSTouchBarItem.Identifier](./identifier-swift.struct/fixedspacelarge.md)
  The identifier of an item appropriate for use as a large space in a Touch Bar.
- [static let flexibleSpace: NSTouchBarItem.Identifier](./identifier-swift.struct/flexiblespace.md)
  The identifier of an item appropriate for use as a flexible space in a Touch Bar.
### Creating identifiers for Touch Bar nesting
- [static let otherItemsProxy: NSTouchBarItem.Identifier](./identifier-swift.struct/otheritemsproxy.md)
  The identifier of the special “other items proxy”, which is used to nest bars up the responder chain.
### Creating identifiers for multiple choice items
- [static let candidateList: NSTouchBarItem.Identifier](./identifier-swift.struct/candidatelist.md)
  The standard identifier for a candidate list bar item.
- [static let characterPicker: NSTouchBarItem.Identifier](./identifier-swift.struct/characterpicker.md)
  The standard identifier for selecting special characters such as Emoji.
### Creating identifiers for text items
- [static let textFormat: NSTouchBarItem.Identifier](./identifier-swift.struct/textformat.md)
  The identifier for a group of text format controls.
- [static let textAlignment: NSTouchBarItem.Identifier](./identifier-swift.struct/textalignment.md)
  The identifier for a Touch Bar item used to select the text alignment.
- [static let textColorPicker: NSTouchBarItem.Identifier](./identifier-swift.struct/textcolorpicker.md)
  The identifier for a Touch Bar item used to select the text color.
- [static let textList: NSTouchBarItem.Identifier](./identifier-swift.struct/textlist.md)
  The identifier for a Touch Bar item used to control the text list style.
- [static let textStyle: NSTouchBarItem.Identifier](./identifier-swift.struct/textstyle.md)
  The identifier for a Touch Bar item used to control the text style.
### Creating a custom identifier
- [init(String)](./identifier-swift.struct/init%28_%29.md)
  Creates an item identifier with the specified custom name.
- [init(rawValue: String)](./identifier-swift.struct/init%28rawvalue%29.md)
  Creates an item identifier with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a bar item
- [init(identifier: NSTouchBarItem.Identifier)](./init%28identifier%29.md)
  Creates a new item with the specified identifier.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Initializes and returns a new item from a storyboard or nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/identifier-swift.struct)*