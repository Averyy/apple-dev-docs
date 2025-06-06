# NSTextLineFragment

**Framework**: AppKit  
**Kind**: class

A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextLineFragment
```

## Topics

### Creating line fragments
- [init(attributedString: NSAttributedString, range: NSRange)](nstextlinefragment/init(attributedstring:range:).md)
  Creates a new line fragment from the attributed string for the range of characters you specify.
- [init?(coder: NSCoder)](nstextlinefragment/init(coder:).md)
  Creates a new line fragment with from data in an unarchiver.
- [convenience init(string: String, attributes: [NSAttributedString.Key : Any], range: NSRange)](nstextlinefragment/init(string:attributes:range:).md)
  Creates a new line fragment using the string, attributes, and range you provide.
### Line fragment characteristics
- [var attributedString: NSAttributedString](nstextlinefragment/attributedstring.md)
  The source attributed string.
- [var characterRange: NSRange](nstextlinefragment/characterrange.md)
  The string range for the source attributed string that corresponds to this line fragment.
- [var glyphOrigin: CGPoint](nstextlinefragment/glyphorigin.md)
  Rendering origin for the left-most glyph in the line fragment coordinate system.
- [var typographicBounds: CGRect](nstextlinefragment/typographicbounds.md)
  The typographic bounds that specifies the dimensions of the line fragment for laying out line fragments to each other.
### Finding specific text
- [func characterIndex(for: CGPoint) -> Int](nstextlinefragment/characterindex(for:).md)
  Returns character index for a point inside the line fragment coordinate system.
- [func fractionOfDistanceThroughGlyph(for: CGPoint) -> CGFloat](nstextlinefragment/fractionofdistancethroughglyph(for:).md)
  Returns character index for a point inside the line fragment coordinate system.
- [func locationForCharacter(at: Int) -> CGPoint](nstextlinefragment/locationforcharacter(at:).md)
  Returns the location of the character at the specified index.
### Drawing
- [func draw(at: CGPoint, in: CGContext)](nstextlinefragment/draw(at:in:).md)
  Renders the line fragment contents at the rendering origin.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Using TextKit 2 to interact with text](../UIKit/using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [class NSTextLayoutManager](nstextlayoutmanager.md)
  The primary class that you use to manage text layout and presentation for custom text displays.
- [class NSTextContainer](nstextcontainer.md)
  A region where text layout occurs.
- [class NSTextLayoutFragment](nstextlayoutfragment.md)
  A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [class NSTextViewportLayoutController](nstextviewportlayoutcontroller.md)
  Manages the layout process inside the viewport interacting with its delegate.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlinefragment)*