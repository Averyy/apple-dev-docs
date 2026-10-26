# NSAttributedStringMarkdownParsingOptions

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

Options that affect the parsing of Markdown content into an attributed string.

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
@interface NSAttributedStringMarkdownParsingOptions : NSObject
```

## Topics

### Creating a Markdown Parsing Options Instance
- [- init](./nsattributedstringmarkdownparsingoptions/init.md)
  Creates a Markdown parsing options instance with the specified values.
### Determining Markdown Parsing Options
- [allowsExtendedAttributes](./nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](./nsattributedstringmarkdownparsingoptions/appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](./nsattributedstringmarkdownparsingoptions/failurepolicy.md)
  The policy for handling a parsing failure.
- [NSAttributedStringMarkdownParsingFailurePolicy](./nsattributedstringmarkdownparsingfailurepolicy.md)
  A type that represents policies for handling parsing failures.
- [interpretedSyntax](./nsattributedstringmarkdownparsingoptions/interpretedsyntax.md)
  The syntax for intepreting a Markdown string.
- [NSAttributedStringMarkdownInterpretedSyntax](./nsattributedstringmarkdowninterpretedsyntax.md)
  A type that represents the syntax for intepreting a Markdown string.
- [languageCode](./nsattributedstringmarkdownparsingoptions/languagecode.md)
  The BCP-47 language code for this document.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](./nscopying.md)

## See Also

### Creating from markdown
- [- initWithMarkdownString:options:baseURL:error:](./nsattributedstring/initwithmarkdownstring_options_baseurl_error_.md)
  Creates an attributed string from a Markdown-formatted string using the provided options.
- [- initWithMarkdown:options:baseURL:error:](./nsattributedstring/initwithmarkdown_options_baseurl_error_.md)
  Creates an attributed string from Markdown-formatted data using the provided options.
- [- initWithContentsOfMarkdownFileAtURL:options:baseURL:error:](./nsattributedstring/initwithcontentsofmarkdownfileaturl_options_baseurl_error_.md)
  Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingoptions)*