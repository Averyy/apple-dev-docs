# init(markdown:options:baseURL:)

**Framework**: Foundation  
**Kind**: init

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

```swift
convenience init(markdown: String, options: AttributedString.MarkdownParsingOptions = .init(), baseURL: URL? = nil) throws
```

## Parameters

- `markdown`: The string that contains the Markdown formatting.
- `options`: Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.
- `baseURL`: The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is  , the initializer doesn’t resolve URLs. The default is  .

## See Also

- [convenience init(markdown: Data, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](nsattributedstring/init(markdown:options:baseurl:)-5nru2.md)
  Creates an attributed string from Markdown-formatted data using the provided options.
- [convenience init(contentsOf: URL, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](nsattributedstring/init(contentsof:options:baseurl:).md)
  Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data using the provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(markdown:options:baseurl:)-m9n)*