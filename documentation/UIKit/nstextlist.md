# NSTextList

**Framework**: UIKit  
**Kind**: class

A section of text that forms a single list.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSTextList
```

#### Overview

The visible elements of the list, including list markers, appear in the text as they do for lists created by hand. The list object, however, allows the list to be recognized as such by the text system. This enables automatic creation of markers and spacing. Text lists are used in HTML import and export.

Text lists appear as attributes on paragraphs, as part of the paragraph style. An [`NSParagraphStyle`](nsparagraphstyle.md) may have an array of text lists, representing the nested lists containing the paragraph, in order from outermost to innermost. For example, if list1 contains four paragraphs, the middle two of which are also in the inner list2, then the text lists array for the first and fourth paragraphs is (list1), while the text lists array for the second and third paragraphs is (list1, list2).

The methods implementing this are [`textLists`](nsparagraphstyle/textlists.md) on [`NSParagraphStyle`](nsparagraphstyle.md), and [`textLists`](nsmutableparagraphstyle/textlists.md) on [`NSMutableParagraphStyle`](nsmutableparagraphstyle.md).

In addition, [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) has convenience methods for lists, such as [`range(of:at:)`](https://developer.apple.com/documentation/Foundation/NSAttributedString/range(of:at:)-6um0x), which determines the range covered by a list, and [`itemNumber(in:at:)`](https://developer.apple.com/documentation/Foundation/NSAttributedString/itemNumber(in:at:)), which determines the ordinal position within a list of a particular item.

## Topics

### Creating a text list
- [init?(coder: NSCoder)](nstextlist/init(coder:).md)
  Initializes and returns a newly allocated text list item.
- [convenience init(markerFormat: NSTextList.MarkerFormat, options: Int)](nstextlist/init(markerformat:options:).md)
  Returns an initialized text list.
- [init(markerFormat: NSTextList.MarkerFormat, options: NSTextList.Options, startingItemNumber: Int)](nstextlist/init(markerformat:options:startingitemnumber:).md)
  Returns a new text list with the format, options, and starting item number you provide.
### Working with markers
- [var markerFormat: NSTextList.MarkerFormat](nstextlist/markerformat-swift.property.md)
  Returns the marker format string used by the receiver.
- [NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct.md)
  Constants that describe marker symbols you can apply to list elements in text lists.
- [func marker(forItemNumber: Int) -> String](nstextlist/marker(foritemnumber:).md)
  Returns the computed value for a specific ordinal position in the list.
### Getting list options
- [var isOrdered: Bool](nstextlist/isordered.md)
- [var listOptions: NSTextList.Options](nstextlist/listoptions.md)
  Returns the list options mask value of the receiver.
- [NSTextList.Options](nstextlist/options.md)
  Values that available options for text list items.
### Managing item numbering
- [var startingItemNumber: Int](nstextlist/startingitemnumber.md)
  Sets the starting item number for the text list.
### Constants
- [static var prependEnclosingMarker: NSTextList.Options](nstextlist/options/prependenclosingmarker.md)
  Specifies that a nested list should include the marker for its enclosing superlist before its own marker.
### Type Properties
- [class var includesTextListMarkers: Bool](nstextlist/includestextlistmarkers.md)

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
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSParagraphStyle](nsparagraphstyle.md)
  The paragraph or ruler attributes for an attributed string.
- [class NSMutableParagraphStyle](nsmutableparagraphstyle.md)
  An object for changing the values of the subattributes in a paragraph style attribute.
- [class NSTextTab](nstexttab.md)
  A tab in a paragraph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlist)*