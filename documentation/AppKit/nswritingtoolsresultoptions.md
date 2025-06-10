# NSWritingToolsResultOptions

**Framework**: AppKit  
**Kind**: struct

Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSWritingToolsResultOptions
```

#### Overview

When configuring a text view, specify what type of text input you want Writing Tools to deliver to your view. You can ask it to return plain text without any attributes, or you can ask it to apply relevant formatting attributes to the text. You can even encourage it to return items in a list or format them in a table.

## Topics

### Getting the output options
- [static var plainText: NSWritingToolsResultOptions](nswritingtoolsresultoptions/plaintext.md)
  An option to allow only plain text without any attributes in the returned text.
- [static var richText: NSWritingToolsResultOptions](nswritingtoolsresultoptions/richtext.md)
  An option to include style attributes consistent with the RTF format in the returned text.
- [static var list: NSWritingToolsResultOptions](nswritingtoolsresultoptions/list.md)
  An option to allow list-style formatting in the returned text.
- [static var table: NSWritingToolsResultOptions](nswritingtoolsresultoptions/table.md)
  An option to allow tabular layout attributes in the returned text.
### Initializers
- [init(rawValue: UInt)](nswritingtoolsresultoptions/init(rawvalue:).md)
### Type Properties
- [static var presentationIntent: NSWritingToolsResultOptions](nswritingtoolsresultoptions/presentationintent.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSCursor.FrameResizePosition](nscursor/frameresizeposition.md)
  The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
- [enum NSHorizontalDirection](nshorizontaldirection.md)
  An absolute direction on the horizontal axis.
- [enum NSSharingCollaborationMode](nssharingcollaborationmode.md)
  Represents the types of sharing (collaborating on an item vs. sending a copy of the item) The share picker supports up to two modes, each of which corresponds to one of these types
- [NSImage.DynamicRange](nsimage/dynamicrange.md)
  Describes how High Dynamic Range (HDR) image content displays.
- [enum NSTextCursorAccessoryPlacement](nstextcursoraccessoryplacement.md)
- [enum NSVerticalDirection](nsverticaldirection.md)
  A direction on the vertical axis.
- [enum NSWritingToolsBehavior](nswritingtoolsbehavior.md)
  Constants that specify the Writing Tools experience for the underlying view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolsresultoptions)*