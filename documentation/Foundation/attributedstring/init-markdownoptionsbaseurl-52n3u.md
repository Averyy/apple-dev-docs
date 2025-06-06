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
init(markdown: String, options: AttributedString.MarkdownParsingOptions = .init(), baseURL: URL? = nil) throws
```

#### Discussion

If your source string includes custom attributes defined by conformers to [`MarkdownDecodableAttributedStringKey`](markdowndecodableattributedstringkey.md) and used with Apple’s markdown extension syntax, be sure to include the [`allowsExtendedAttributes`](nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) option. Otherwise, the initializer doesn’t parse these attributes.

## Parameters

- `markdown`: The string that contains the Markdown formatting.
- `options`: Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.
- `baseURL`: The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is  , the initializer doesn’t resolve URLs. The default is  .

## See Also

- [init<S>(markdown: String, including: S.Type, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](attributedstring/init(markdown:including:options:baseurl:)-4m51b.md)
  Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope.
- [init<S>(markdown: String, including: KeyPath<AttributeScopes, S.Type>, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](attributedstring/init(markdown:including:options:baseurl:)-89e48.md)
  Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope that a key path identifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(markdown:options:baseurl:)-52n3u)*