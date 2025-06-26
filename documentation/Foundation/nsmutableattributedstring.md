# NSMutableAttributedString

**Framework**: Foundation  
**Kind**: class

A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSMutableAttributedString
```

#### Overview

The `NSMutableAttributedString` class declares additional methods for mutating the content of an attributed string. You can add and remove characters (raw strings) and attributes separately or together as attributed strings. See the class description for [`NSAttributedString`](nsattributedstring.md) for more information about attributed strings.

`NSMutableAttributedString` adds two primitive methods to those of `NSAttributedString`. These primitive methods provide the basis for all the other methods in its class. The primitive [`replaceCharacters(in:with:)`](nsmutableattributedstring/replacecharacters(in:with:)-6oq9r.md) method replaces a range of characters with those from a string, leaving all attribute information outside that range intact. The primitive [`setAttributes(_:range:)`](nsmutableattributedstring/setattributes(_:range:).md) method sets attributes and values for a given range of characters, replacing any previous attributes and values for that range.

In macOS, AppKit also uses [`NSParagraphStyle`](https://developer.apple.com/documentation/AppKit/NSParagraphStyle) and its subclass [`NSMutableParagraphStyle`](https://developer.apple.com/documentation/AppKit/NSMutableParagraphStyle) to encapsulate the paragraph or ruler attributes used by the `NSAttributedString` classes.

Note that the default font for `NSAttributedString` objects is Helvetica 12-point, which may differ from the macOS system font, so you may wish to create the string with non-default attributes suitable for your application using, for example, [`init(string:attributes:)`](nsattributedstring/init(string:attributes:).md).

> **Note**:  In iOS, this class is used primarily in conjunction with the Core Text framework.

`NSMutableAttributedString` is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableAttributedString`](https://developer.apple.com/documentation/CoreFoundation/CFMutableAttributedString). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

## Topics

### Retrieving Character Information
- [var mutableString: NSMutableString](nsmutableattributedstring/mutablestring.md)
  The character contents of the receiver as a mutable string object.
### Changing Characters
- [func replaceCharacters(in: NSRange, with: String)](nsmutableattributedstring/replacecharacters(in:with:)-6oq9r.md)
  Replaces the characters in the given range with the characters of the given string.
- [func deleteCharacters(in: NSRange)](nsmutableattributedstring/deletecharacters(in:).md)
  Deletes the characters in the given range along with their associated attributes.
### Changing Attributes
- [func setAttributes([NSAttributedString.Key : Any]?, range: NSRange)](nsmutableattributedstring/setattributes(_:range:).md)
  Sets the attributes for the characters in the specified range to the specified attributes.
- [func addAttribute(NSAttributedString.Key, value: Any, range: NSRange)](nsmutableattributedstring/addattribute(_:value:range:).md)
  Adds an attribute with the given name and value to the characters in the specified range.
- [func addAttributes([NSAttributedString.Key : Any], range: NSRange)](nsmutableattributedstring/addattributes(_:range:).md)
  Adds the given collection of attributes to the characters in the specified range.
- [func removeAttribute(NSAttributedString.Key, range: NSRange)](nsmutableattributedstring/removeattribute(_:range:).md)
  Removes the named attribute from the characters in the specified range.
- [func applyFontTraits(NSFontTraitMask, range: NSRange)](nsmutableattributedstring/applyfonttraits(_:range:).md)
  Applies the specified font-related attributes to characters in the string.
- [func setAlignment(NSTextAlignment, range: NSRange)](nsmutableattributedstring/setalignment(_:range:).md)
  Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](nsmutableattributedstring/setbasewritingdirection(_:range:).md)
  Sets the base writing direction for the characters to the specified direction.
- [func subscriptRange(NSRange)](nsmutableattributedstring/subscriptrange(_:).md)
  Decrements the value of the superscript attribute for characters in the specified range by one.
- [func superscriptRange(NSRange)](nsmutableattributedstring/superscriptrange(_:).md)
  Increments the value of the superscript attribute for characters in the specified range by one.
- [func unscriptRange(NSRange)](nsmutableattributedstring/unscriptrange(_:).md)
  Removes the superscript attribute from the characters in the specified range.
### Changing Characters and Attributes
- [func append(NSAttributedString)](nsmutableattributedstring/append(_:).md)
  Adds the characters and attributes of a given attributed string to the end of the receiver.
- [func insert(NSAttributedString, at: Int)](nsmutableattributedstring/insert(_:at:).md)
  Inserts the characters and attributes of the given attributed string into the receiver at the given index.
- [func replaceCharacters(in: NSRange, with: NSAttributedString)](nsmutableattributedstring/replacecharacters(in:with:)-1uaw7.md)
  Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.
- [func setAttributedString(NSAttributedString)](nsmutableattributedstring/setattributedstring(_:).md)
  Replaces the receiver’s entire contents with the characters and attributes of the given attributed string.
### Grouping Changes
- [func beginEditing()](nsmutableattributedstring/beginediting.md)
  Begins the buffering of changes to the string’s characters and attributes.
- [func endEditing()](nsmutableattributedstring/endediting.md)
  Ends the buffering of changes to the string’s characters and attributes.
### Updating Attachment Contents
- [func updateAttachments(fromPath: String)](nsmutableattributedstring/updateattachments(frompath:).md)
  Updates all attachments based on files contained in the RTFD file package at the specified file path.
### Fixing Attributes After Changes
- [func fixAttributes(in: NSRange)](nsmutableattributedstring/fixattributes(in:).md)
  Cleans up font, paragraph style, and attachment attributes within the given range.
- [func fixAttachmentAttribute(in: NSRange)](nsmutableattributedstring/fixattachmentattribute(in:).md)
  Cleans up attachment attributes in the specified range and removes all attachment attributes assigned to characters except the designated attachment character.
- [func fixFontAttribute(in: NSRange)](nsmutableattributedstring/fixfontattribute(in:).md)
  Fixes the font attribute in the specified range and assigns default fonts where appropriate.
- [func fixParagraphStyleAttribute(in: NSRange)](nsmutableattributedstring/fixparagraphstyleattribute(in:).md)
  Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.
### Reading Content
- [func read(from: Data, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsmutableattributedstring/read(from:options:documentattributes:)-5mbcx.md)
  Sets the contents of the attributed string using the specified data object`.`
- [func read(from: URL, options: [NSAttributedString.DocumentReadingOptionKey : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsmutableattributedstring/read(from:options:documentattributes:)-54wth.md)
  Sets the contents of attributed string using the contents of the specified file.
### Deprecated
- [func read(from: Data, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](nsmutableattributedstring/read(from:options:documentattributes:)-967j7.md)
  Sets the contents of the receiver from the specified data object`.`
- [func read(from: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](nsmutableattributedstring/read(from:options:documentattributes:)-85y1d.md)
  Sets the contents of receiver from the file at the specified URL.
- [func read(fromFileURL: URL, options: [AnyHashable : Any], documentAttributes: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) throws](nsmutableattributedstring/read(fromfileurl:options:documentattributes:).md)
  Sets the contents of the receiver from the file at the given URL.

## Relationships

### Inherits From
- [NSAttributedString](nsattributedstring.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AttributedString](attributedstring.md)
  A value type for a string with associated attributes for portions of its text.
- [struct AttributedSubstring](attributedsubstring.md)
  A portion of an attributed string.
- [Attributed String Supporting Types](attributed-string-supporting-types.md)
  Types that the attributed string, attributed substring, and helper types extend or conform to, for sharing common functionality.
- [class NSAttributedString](nsattributedstring.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring)*