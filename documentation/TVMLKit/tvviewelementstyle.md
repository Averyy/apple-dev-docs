# TVViewElementStyle

**Framework**: TVMLKit  
**Kind**: class

A style applied to a view element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVViewElementStyle
```

## Topics

### Retrieving the Style for an Element
- [func value(propertyName: String) -> Any?](tvviewelementstyle/value(propertyname:).md)
  Returns the value associated with a given style name.
### Defining the Height and Width of an Element
- [var height: CGFloat](tvviewelementstyle/height.md)
  The height, in pixels, for an element.
- [var maxHeight: CGFloat](tvviewelementstyle/maxheight.md)
  The maximum height, in pixels, for the element.
- [var maxWidth: CGFloat](tvviewelementstyle/maxwidth.md)
  The maximum width, in pixels, for an element.
- [var minHeight: CGFloat](tvviewelementstyle/minheight.md)
  The minimum height, in pixels, for an element.
- [var minWidth: CGFloat](tvviewelementstyle/minwidth.md)
  The minimum width, in pixels, for an element.
- [var width: CGFloat](tvviewelementstyle/width.md)
  The width, in pixels, for an element.
### Aligning and Positioning an Element
- [var alignment: TVElementAlignment](tvviewelementstyle/alignment.md)
  A value indicating how an item is aligned inside of an element.
- [enum TVElementAlignment](tvelementalignment.md)
  Location of an item inside of an element on the horizontal axis.
- [var contentAlignment: TVElementContentAlignment](tvviewelementstyle/contentalignment.md)
  A value indicating how items inside of an element are aligned.
- [enum TVElementContentAlignment](tvelementcontentalignment.md)
  Location of items inside of an element on the vertical axis.
- [var focusMargin: UIEdgeInsets](tvviewelementstyle/focusmargin.md)
  The amount of space, in pixels, a custom cell requires when it comes into focus.
- [var interitemSpacing: CGFloat](tvviewelementstyle/interitemspacing.md)
  The spacing, in pixels, between items inside of an element.
- [var margin: UIEdgeInsets](tvviewelementstyle/margin.md)
  The amount of space, in pixels, between the element and other elements.
- [var padding: UIEdgeInsets](tvviewelementstyle/padding.md)
  The amount of space, in pixels, between the border and the contents of the element.
- [var position: TVElementPosition](tvviewelementstyle/position.md)
  A value indicating the position of the element relative to the screen or its containing element.
- [enum TVElementPosition](tvelementposition.md)
  Location of an element relative to the screen or its containing element.
### Changing the Text of an Element
- [var fontSize: CGFloat](tvviewelementstyle/fontsize.md)
  The font size applied to any text contained in the element.
- [var fontWeight: String?](tvviewelementstyle/fontweight.md)
  A string indicating how thick or thin the font is.
- [var maxTextLines: Int](tvviewelementstyle/maxtextlines.md)
  The maximum number of lines of text allowed inside of the element.
- [var textAlignment: NSTextAlignment](tvviewelementstyle/textalignment.md)
  The horizontal alignment of text within an element.
- [var textHighlightStyle: String?](tvviewelementstyle/texthighlightstyle.md)
  A string indicating how a label reacts when it is in focus.
- [var textMinimumScaleFactor: CGFloat](tvviewelementstyle/textminimumscalefactor.md)
  The minimum size text can be if the original text size does not fit in an element.
- [var textStyle: String?](tvviewelementstyle/textstyle.md)
  The style applied to the text in an element.
### Modifying an Image
- [var imageTreatmentName: String?](tvviewelementstyle/imagetreatmentname.md)
  A value that determines how an image is displayed.
- [var ratingStyle: String?](tvviewelementstyle/ratingstyle.md)
  A string indicating the style to be used by a rating element.
### Coloring an Element
- [var backgroundColor: TVColor?](tvviewelementstyle/backgroundcolor.md)
  The background color for an element.
- [var color: TVColor?](tvviewelementstyle/color.md)
  The color for an element.
- [var highlightColor: TVColor?](tvviewelementstyle/highlightcolor.md)
  The color of the element when it is highlighted.
- [var tintColor: TVColor?](tvviewelementstyle/tintcolor.md)
  The tint color applied to an element.
### Element Styles
- [Transition Style Values](transition-style-values.md)
  The type of transition to apply to an element.
- [Rating Style Values](rating-style-values.md)
  The size of the star image used for a rating element.
- [Label State Values](label-state-values.md)
  How text is displayed when an element is in focus.
- [Text Style Values](text-style-values.md)
  Font size and weight.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVStyleFactory](tvstylefactory.md)
  An object used to register custom style properties.
- [class TVColor](tvcolor.md)
  The color data used by styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyle)*