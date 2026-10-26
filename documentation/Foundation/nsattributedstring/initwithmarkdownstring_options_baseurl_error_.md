# initWithMarkdownString:options:baseURL:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates an attributed string from a Markdown-formatted string using the provided options.

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
- (instancetype) initWithMarkdownString:(NSString *) markdownString options:(NSAttributedStringMarkdownParsingOptions *) options baseURL:(NSURL *) baseURL error:(NSError **) error;
```

#### Return Value

An attributed string with the parsed Markdown text and styling, or `nil` if parsing the data fails.

## Parameters

- `markdownString`: The string that contains the Markdown formatting.
- `options`: Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.
- `baseURL`: The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is `nil`, the initializer doesn’t resolve URLs. The default is `nil`.
- `error`: On input, a pointer to an error object. On return, if an error occurs, this pointer contains an actual error object with the error information. You may specify `nil` for this parameter if you don’t want the error information.

## See Also

### Creating from markdown
- [- initWithMarkdown:options:baseURL:error:](./initwithmarkdown_options_baseurl_error_.md)
  Creates an attributed string from Markdown-formatted data using the provided options.
- [- initWithContentsOfMarkdownFileAtURL:options:baseURL:error:](./initwithcontentsofmarkdownfileaturl_options_baseurl_error_.md)
  Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.
- [NSAttributedStringMarkdownParsingOptions](../nsattributedstringmarkdownparsingoptions.md)
  Options that affect the parsing of Markdown content into an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/initwithmarkdownstring:options:baseurl:error:)*