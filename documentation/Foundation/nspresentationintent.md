# NSPresentationIntent

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A type that contains the Markdown formatting for blocks of text, like paragraphs, lists, code blocks, and parts of tables.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@interface NSPresentationIntent : NSObject
```

#### Overview

An [`NSPresentationIntent`](./nspresentationintent.md) object stores the Markdown semantics for a range of characters in an attributed string. When parsing Markdown into an attributed string, the system sets the value of the [`presentationIntentAttributeName`](./nsattributedstring/key/presentationintentattributename.md) attribute to an instance of this class. When displaying your string in system views, the system applies a default visual style to match the corresponding information in this type. To replace the system’s default formatting, remove these attributes from your attributed string and apply the formatting you want.

## Topics

### Creating a presentation intent
- [+ paragraphIntentWithIdentity:nestedInsideIntent:](./nspresentationintent/paragraphintentwithidentity_nestedinsideintent_.md)
  Creates a  paragraph intent with the provided information.
- [+ headerIntentWithIdentity:level:nestedInsideIntent:](./nspresentationintent/headerintentwithidentity_level_nestedinsideintent_.md)
  Creates a header intent with the provided information.
- [+ orderedListIntentWithIdentity:nestedInsideIntent:](./nspresentationintent/orderedlistintentwithidentity_nestedinsideintent_.md)
  Creates an ordered-list intent with the provided information.
- [+ unorderedListIntentWithIdentity:nestedInsideIntent:](./nspresentationintent/unorderedlistintentwithidentity_nestedinsideintent_.md)
  Creates an unordered-list intent with the provided information.
- [+ listItemIntentWithIdentity:ordinal:nestedInsideIntent:](./nspresentationintent/listitemintentwithidentity_ordinal_nestedinsideintent_.md)
  Creates an item for an ordered list with the provided information.
- [+ codeBlockIntentWithIdentity:languageHint:nestedInsideIntent:](./nspresentationintent/codeblockintentwithidentity_languagehint_nestedinsideintent_.md)
  Creates an code-block intent with the provided information.
- [+ blockQuoteIntentWithIdentity:nestedInsideIntent:](./nspresentationintent/blockquoteintentwithidentity_nestedinsideintent_.md)
  Creates a block-quote intent with the provided information.
- [+ thematicBreakIntentWithIdentity:nestedInsideIntent:](./nspresentationintent/thematicbreakintentwithidentity_nestedinsideintent_.md)
  Creates a thematic break intent with the provided information.
- [+ tableIntentWithIdentity:columnCount:alignments:nestedInsideIntent:](./nspresentationintent/tableintentwithidentity_columncount_alignments_nestedinsideintent_.md)
  Creates a table intent with the provided information.
- [+ tableHeaderRowIntentWithIdentity:nestedInsideIntent:](./nspresentationintent/tableheaderrowintentwithidentity_nestedinsideintent_.md)
  Creates a table header intent with the provided information.
- [+ tableRowIntentWithIdentity:row:nestedInsideIntent:](./nspresentationintent/tablerowintentwithidentity_row_nestedinsideintent_.md)
  Creates a table row intent with the provided information.
- [+ tableCellIntentWithIdentity:column:nestedInsideIntent:](./nspresentationintent/tablecellintentwithidentity_column_nestedinsideintent_.md)
  Creates a table cell intent with the provided information.
### Getting the intent identity
- [identity](./nspresentationintent/identity.md)
  A unique identifier for the intent in the document.
- [intentKind](./nspresentationintent/intentkind.md)
  The type of the intent.
- [parentIntent](./nspresentationintent/parentintent.md)
  The parent of the current intent.
- [- isEquivalentToPresentationIntent:](./nspresentationintent/isequivalenttopresentationintent_.md)
  Returns a Boolean value that indicates whether the current intent is equivalent to the specified intent.
### Getting header information
- [headerLevel](./nspresentationintent/headerlevel.md)
  The level of a header section.
### Getting list information
- [ordinal](./nspresentationintent/ordinal.md)
  The number for an item in an ordered list.
- [indentationLevel](./nspresentationintent/indentationlevel.md)
  The indentation level of the intent.
### Getting table information
- [row](./nspresentationintent/row.md)
  The row number to which this cell belongs.
- [column](./nspresentationintent/column.md)
  The column number to which the cell belongs.
- [columnCount](./nspresentationintent/columncount.md)
  The number of columns in a table.
- [columnAlignments](./nspresentationintent/columnalignments.md)
  The alignments for the columns in a table.
### Getting code information
- [languageHint](./nspresentationintent/languagehint.md)
  The language associated with the code listing.

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
- [NSAttributedStringMarkdownSourcePosition](./nsattributedstringmarkdownsourceposition.md)
  The position of attributed string text in its original Markdown source string.
- [NSPresentationIntentKind](./nspresentationintentkind.md)
  An enumeration of intended display styles for blocks of text like paragraphs, lists, and code blocks.
- [NSPresentationIntentTableColumnAlignment](./nspresentationintenttablecolumnalignment.md)
  An enumeration of values for aligning the contents of table columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspresentationintent)*