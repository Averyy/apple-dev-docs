# NSAttributedStringMarkdownSourcePosition

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

The position of attributed string text in its original Markdown source string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```objc
@interface NSAttributedStringMarkdownSourcePosition : NSObject
```

## Topics

### Creating an Attributed String Markdown Source Position Instance
- [- initWithStartLine:startColumn:endLine:endColumn:](./nsattributedstringmarkdownsourceposition/initwithstartline_startcolumn_endline_endcolumn_.md)
  Creates a Markdown source position instance from its start and end line and column.
### Getting Markdown Source Position Properties
- [startLine](./nsattributedstringmarkdownsourceposition/startline.md)
  The line where the text begins in the Markdown source.
- [startColumn](./nsattributedstringmarkdownsourceposition/startcolumn.md)
  The column where the text begins in the Markdown source.
- [endLine](./nsattributedstringmarkdownsourceposition/endline.md)
  The line where the text ends in the Markdown source.
- [endColumn](./nsattributedstringmarkdownsourceposition/endcolumn.md)
  The column where the text ends in the Markdown source.
### Getting a Range from a Markdown Source Position Attribute
- [- rangeInString:](./nsattributedstringmarkdownsourceposition/rangeinstring_.md)
  Returns a range indicating the source portion within a Markdown string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](./nscopying.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Representing markdown attributes
- [struct InlinePresentationIntent](./inlinepresentationintent.md)
  A type that defines presentation intent for runs of characters for traits like emphasis, strikethrough, and code voice.
- [NSPresentationIntent](./nspresentationintent.md)
  A type that contains the Markdown formatting for blocks of text, like paragraphs, lists, code blocks, and parts of tables.
- [NSPresentationIntentKind](./nspresentationintentkind.md)
  An enumeration of intended display styles for blocks of text like paragraphs, lists, and code blocks.
- [NSPresentationIntentTableColumnAlignment](./nspresentationintenttablecolumnalignment.md)
  An enumeration of values for aligning the contents of table columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownsourceposition)*