# NSAttributedString

**Framework**: Foundation  
**Kind**: class

A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.

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
class NSAttributedString
```

#### Overview

[`NSAttributedString`](nsattributedstring.md) is a type you use to manage strings of stylized Unicode text. In addition to text, an attributed string contains key-value pairs known as  that specify additional information to apply to ranges of characters within the string. Attributed strings support many different kinds of attributes, including:

- Rendering attributes that specify font, color, kern, ligature, and other details
- Attributes for attachments and adaptive image glyphs
- Semantic attributes such as link URLs or tool-tip information
- Language attributes to support automatic gender agreement and text layout
- Accessibility attributes that provide information for assistive technologies
- Attributes that summarize details of the Markdown import process
- Custom attributes you define for your app

Use attributed strings anywhere you need styled text, or when you need to associate additional information with your text. Because [`NSAttributedString`](nsattributedstring.md) is an immutable type, you specify all of the text and attributes for it at creation time and can’t change them later. You can create attributed strings directly from a string of characters and a dictionary of attributes. You can also create attributed strings from the contents of a file, including files that contain RTF, RTFD, HTML, Markdown, or other file formats. If you need to modify the contents of an attributed string later, use the [`NSMutableAttributedString`](nsmutableattributedstring.md) type instead.

If you create an [`NSAttributedString`](nsattributedstring.md) without any font information, the string’s default font is Helvetica 12-point, which might differ from the default system font for the platform. To change the font, specify a font attribute at creation time.

##### Persistence

Be aware of how you persist attributed strings to and from the disk. RTF and RTFD are the preferred format for attributed strings because they offer the best fidelity for reading and writing attribute data. The RTF formats support a large number of standard attributes, and Apple extends the formats to support many Apple-specific attributes. If you define custom attributes for ranges of characters, store them separately alongside the RTF file for your text.

If you work extensively with HTML content, validate the results and performance of import and export operations during testing. WebKit handles the conversion between HTML markup and attributed strings. If an HTML file contains tags or constructs that attributed strings don’t support, the import process ignores them and imports what it can.

When you create an attributed string from Markdown, the system adds presentation intent attributes with information about the original Markdown content. The system doesn’t add style attributes to match the Markdown elements, but the system applies default style information when it renders a string with intent attributes. To change the rendering behavior of your Markdown content, remove the intent attributes and add the style attributes you prefer.

> ❗ **Important**:  When reading or writing attributed strings, choose methods that return or throw an error, and check any errors you receive. Handling errors is the best way to detect issues with the import or export process and take corrective action.

The methods for reading and writing common file formats also support document attributes. Document attributes aren’t part of the attributed string itself, but accompany the text when you save it to a file. When you read a file, the system returns any document attributes that it finds. Similarly, when you write an attributed string to a file, you can specify the attributes to include. For more information about document attributes, see [`NSAttributedString.DocumentAttributeKey`](nsattributedstring/documentattributekey.md) and [`NSAttributedString.DocumentReadingOptionKey`](nsattributedstring/documentreadingoptionkey.md).

##### System Framework Interoperability

[`TextKit`](https://developer.apple.com/documentation/UIKit/textkit) and [`Core Text`](https://developer.apple.com/documentation/CoreText) use attributed strings extensively during the layout and rendering processes. These technologies use the string’s text and rendering-related attributes to calculate the text metrics needed during layout. Similarly, these technologies apply those same attributes during rendering to give the text its styled appearance. The technologies use only attributes that directly affect the appearance of the text, and ignore most other attributes. For some attributes, the text system adds attributes during rendering as needed. For example, the text system provides default style attributes for text with the [`link`](nsattributedstring/key/link.md) attribute.

[`AppKit`](https://developer.apple.com/documentation/AppKit) and [`UIKit`](https://developer.apple.com/documentation/UIKit) also support attributed strings in several ways. Some views and controls in these frameworks have APIs that accept attributed strings, and render the string with its style information. The frameworks also add methods to the [`NSAttributedString`](nsattributedstring.md) class that let you draw a styled string directly in one of your custom views. Because these methods use TextKit to draw the string, they recognize the same rendering-related attributes as that technology.

The [`NSAttributedString`](nsattributedstring.md) class and its Core Foundation counterpart, [`CFAttributedString`](https://developer.apple.com/documentation/CoreFoundation/CFAttributedString), are toll-free bridged, which means you can use the two types interchangeably in your code without losing any text or attribute information.

## Topics

### Creating attributed strings
- [Creation methods](creation-methods.md)
  Create attributed strings from existing content or raw text and apply the initial attributes.
### Exporting the string as data
- [func data(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> Data](nsattributedstring/data(from:documentattributes:).md)
  Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func fileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> FileWrapper](nsattributedstring/filewrapper(from:documentattributes:).md)
  Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func docFormat(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](nsattributedstring/docformat(from:documentattributes:).md)
  Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [func rtf(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](nsattributedstring/rtf(from:documentattributes:).md)
  Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [func rtfd(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](nsattributedstring/rtfd(from:documentattributes:).md)
  Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [func rtfdFileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> FileWrapper?](nsattributedstring/rtfdfilewrapper(from:documentattributes:).md)
  Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.
### Getting the characters
- [var string: String](nsattributedstring/string.md)
  The character contents of the attributed string as a string.
- [var length: Int](nsattributedstring/length.md)
  The length of the attributed string.
- [func attributedSubstring(from: NSRange) -> NSAttributedString](nsattributedstring/attributedsubstring(from:).md)
  Returns an attributed string consisting of the characters and attributes within the specified range in the attributed string.
### Getting font attribute information
- [func fontAttributes(in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/fontattributes(in:).md)
  Returns the font attributes in effect for the character at the specified location.
- [func rulerAttributes(in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/rulerattributes(in:).md)
  Returns the ruler (paragraph) attributes in effect for the characters within the specified range.
### Getting attributes for a range of text
- [func attributes(at: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:effectiverange:).md)
  Returns the attributes for the character at the specified index.
- [func attributes(at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:longesteffectiverange:in:).md)
  Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [func attribute(NSAttributedString.Key, at: Int, effectiveRange: NSRangePointer?) -> Any?](nsattributedstring/attribute(_:at:effectiverange:).md)
  Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func attribute(NSAttributedString.Key, at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](nsattributedstring/attribute(_:at:longesteffectiverange:in:).md)
  Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttribute(NSAttributedString.Key, in: NSRange, options: NSAttributedString.EnumerationOptions, using: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattribute(_:in:options:using:).md)
  Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [func enumerateAttributes(in: NSRange, options: NSAttributedString.EnumerationOptions, using: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattributes(in:options:using:).md)
  Executes the specified closure or block for each range of attributes in the attributed string.
- [NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions.md)
  Options for enumerating attributes.
### Getting text content attributes
- [NSAttributedString.Key](nsattributedstring/key.md)
  The attributes you apply to ranges of characters in an attributed string.
- [NSAttributedString.TextHighlightStyle](nsattributedstring/texthighlightstyle.md)
  Constants that specify the type of highlight to apply to text.
- [NSAttributedString.TextHighlightColorScheme](nsattributedstring/texthighlightcolorscheme.md)
  Constants that specify the highlight color to use with the text.
- [NSAttributedString.TextEffectStyle](nsattributedstring/texteffectstyle.md)
  Constants for the type of effect to apply to the text.
- [NSAttributedString.SpellingState](nsattributedstring/spellingstate.md)
  Constants for the spelling state attribute key.
- [struct NSUnderlineStyle](../UIKit/NSUnderlineStyle.md)
  Constants for the underline style and strikethrough style attribute keys.
- [enum NSWritingDirectionFormatType](../UIKit/NSWritingDirectionFormatType.md)
  Constants for the writing direction attribute key.
### Getting document-wide attributes
- [NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey.md)
  The attributes you apply to an entire document.
- [NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey.md)
  Options for constructing an attributed string from data you read from disk.
- [HTML attributes](html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.DocumentType](nsattributedstring/documenttype.md)
  Constants for the document type document attribute key.
- [NSAttributedString.TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.
- [enum NSTextScalingType](../UIKit/NSTextScalingType.md)
  Constants that specify the text scaling.
### Representing markdown attributes
- [struct InlinePresentationIntent](inlinepresentationintent.md)
  A type that defines presentation intent for runs of characters for traits like emphasis, strikethrough, and code voice.
### Comparing strings
- [func isEqual(to: NSAttributedString) -> Bool](nsattributedstring/isequal(to:).md)
  Returns a Boolean value that indicates whether the attributed string is equal to the specified string.
### Getting the supported text-file formats
- [func prefersRTFD(in: NSRange) -> Bool](nsattributedstring/prefersrtfd(in:).md)
  Returns a Boolean value that indicates whether the specified range of text prefers RTFD formatting.
- [class var textTypes: [String]](nsattributedstring/texttypes.md)
  An array of UTI strings that identify the file types that attributed strings support, either directly or through a user-installed filter service.
- [class var textUnfilteredTypes: [String]](nsattributedstring/textunfilteredtypes.md)
  An array of UTI strings that identify the file types that attributed strings support directly.
### Calculating linguistic units
- [func doubleClick(at: Int) -> NSRange](nsattributedstring/doubleclick(at:).md)
  Returns the range of characters that form a word (or other linguistic unit) surrounding the specified index, taking language characteristics into account.
- [func lineBreak(before: Int, within: NSRange) -> Int](nsattributedstring/linebreak(before:within:).md)
  Returns the appropriate line break when the character at the index doesn’t fit on the same line as the character at the beginning of the range.
- [func lineBreakByHyphenating(before: Int, within: NSRange) -> Int](nsattributedstring/linebreakbyhyphenating(before:within:).md)
  Returns the index of the closest character before the specified index, and within the specified range, that can fit on a new line by hyphenating.
- [func nextWord(from: Int, forward: Bool) -> Int](nsattributedstring/nextword(from:forward:).md)
  Returns the index of the first character of the word after or before the specified index.
### Performing automatic grammar agreement
- [func inflecting() -> NSAttributedString](nsattributedstring/inflecting.md)
### Calculating ranges for common elements
- [func itemNumber(in: NSTextList, at: Int) -> Int](nsattributedstring/itemnumber(in:at:).md)
  Returns the index of the item at the specified location within the list.
- [func range(of: NSTextBlock, at: Int) -> NSRange](nsattributedstring/range(of:at:)-1wrcp.md)
  Returns the range of the individual text block that contains the specified location.
- [func range(of: NSTextList, at: Int) -> NSRange](nsattributedstring/range(of:at:)-6um0x.md)
  Returns the range of the specified text list that contains the specified location.
- [func range(of: NSTextTable, at: Int) -> NSRange](nsattributedstring/range(of:at:)-3fevu.md)
  Returns the range of the specified text table that contains the specified location.
### Drawing the attributed string
- [func draw(at: CGPoint)](nsattributedstring/draw(at:).md)
  Draws the attributed string starting at the specified point in the current graphics context.
- [func draw(in: CGRect)](nsattributedstring/draw(in:).md)
  Draws the attributed string inside the specified bounding rectangle in the current graphics context.
- [func draw(with: CGRect, options: NSStringDrawingOptions, context: NSStringDrawingContext?)](nsattributedstring/draw(with:options:context:).md)
  Draws the attributed string in the specified bounding rectangle using the provided options.
### Getting metrics for the string
- [func size() -> CGSize](nsattributedstring/size.md)
  Returns the size necessary to draw the string.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, context: NSStringDrawingContext?) -> CGRect](nsattributedstring/boundingrect(with:options:context:).md)
  Returns the bounding rectangle necessary to draw the string.
- [func containsAttachments(in: NSRange) -> Bool](nsattributedstring/containsattachments(in:).md)
  Returns a Boolean value that indicates if the attributed string contains an attachment in the specified range.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Migrate your code away from using these symbols.
### Initializers
- [init?(pasteboardPropertyList: Any, ofType: NSPasteboard.PasteboardType)](nsattributedstring/init(pasteboardpropertylist:oftype:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableAttributedString](nsmutableattributedstring.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSItemProviderReading](nsitemproviderreading.md)
- [NSItemProviderWriting](nsitemproviderwriting.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSPasteboardReading](../AppKit/NSPasteboardReading.md)
- [NSPasteboardWriting](../AppKit/NSPasteboardWriting.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [struct AttributedString](attributedstring.md)
  A value type for a string with associated attributes for portions of its text.
- [struct AttributedSubstring](attributedsubstring.md)
  A portion of an attributed string.
- [Attributed String Supporting Types](attributed-string-supporting-types.md)
  Types that the attributed string, attributed substring, and helper types extend or conform to, for sharing common functionality.
- [class NSMutableAttributedString](nsmutableattributedstring.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring)*