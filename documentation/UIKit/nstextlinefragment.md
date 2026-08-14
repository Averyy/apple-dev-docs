# NSTextLineFragment

**Framework**: UIKit  
**Kind**: class

A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md)
  Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)
  Customize layout and preserve attachment views in your text view subclass.
- [class NSTextLayoutManager](nstextlayoutmanager.md)
  The primary class that you use to manage text layout and presentation for custom text displays.
- [class NSTextContainer](nstextcontainer.md)
  A region where text layout occurs.
- [class NSTextLayoutFragment](nstextlayoutfragment.md)
  A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [class NSTextViewportLayoutController](nstextviewportlayoutcontroller.md)
  Manages the layout process inside the viewport interacting with its delegate.
- [protocol NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md)
  A protocol that identifies a view or layer as a drawable element for a text layout fragment.
- [protocol NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md)
  A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlinefragment)*