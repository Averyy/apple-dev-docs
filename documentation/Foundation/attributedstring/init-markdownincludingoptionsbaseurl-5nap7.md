# init(markdown:including:options:baseURL:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string from Markdown-formatted data using the provided options and attribute scope that a key path identifies.

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
init<S>(markdown: Data, including scope: KeyPath<AttributeScopes, S.Type>, options: AttributedString.MarkdownParsingOptions = .init(), baseURL: URL? = nil) throws where S : AttributeScope
```

#### Discussion

If your source string includes custom attributes defined by conformers to [`MarkdownDecodableAttributedStringKey`](markdowndecodableattributedstringkey.md) and used with Apple’s markdown extension syntax, be sure to include the [`allowsExtendedAttributes`](nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) option. Otherwise, the initializer doesn’t parse these attributes.

## Parameters

- `markdown`: The   instance that contains the Markdown formatting.
- `scope`: The   key path that identifies an attribute scope to associate with the attributed string.
- `options`: Options that affect how the initializer interprets formatting in the Markdown string. This parameter defaults to no options.
- `baseURL`: The base URL to use when resolving Markdown URLs. The initializer treats URLs as being relative to this URL. If this value is  , the initializer doesn’t resolve URLs. The default is  .

## See Also

- [init(markdown: Data, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](attributedstring/init(markdown:options:baseurl:)-2sg1o.md)
  Creates an attributed string from Markdown-formatted data using the provided options.
- [init<S>(markdown: Data, including: S.Type, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](attributedstring/init(markdown:including:options:baseurl:)-4co46.md)
  Creates an attributed string from Markdown-formatted data using the provided options and attribute scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(markdown:including:options:baseurl:)-5nap7)*