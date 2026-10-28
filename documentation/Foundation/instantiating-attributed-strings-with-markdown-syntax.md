# Instantiating Attributed Strings with Markdown Syntax

**Framework**: Foundation  
**Role**: API Collection

Use a Markdown-syntax string to iniitalize an attributed string with standard or custom attributes.

## Overview

You can use familiar Markdown syntax to initialize an attributed string with both its initial text and attributes for things like inline styles and links. In many cases, this produces easier-to-read code than manually setting attributes on ranges of an existing attributed string.

```swift
if let attString = try? AttributedString(
    markdown: "See the *latest* news at [our website](https://example.com)."),
    let websiteRange = attString.range(of: "our website"),
    let link = attString[websiteRange].link {
    print("\(link)") // Prints "https://example.com".
}
```

In this example, `attString` contains five runs, with attributes parsed from the syntax in the `markdown` parameter:

- `“See the “`, with no attributes.
- `“latest”`, with an [`AttributeScopes.FoundationAttributes.InlinePresentationIntentAttribute`](./attributescopes/foundationattributes/inlinepresentationintentattribute.md) whose value is [`emphasized`](./inlinepresentationintent/emphasized.md).
- `“ news at “`, with no attributes.
- `“our website”`, with an [`AttributeScopes.FoundationAttributes.LinkAttribute`](./attributescopes/foundationattributes/linkattribute.md) whose value is a [`URL`](./url.md).
- `“.”`, with no attributes.

You can also use custom attributes defined with the [`MarkdownDecodableAttributedStringKey`](./markdowndecodableattributedstringkey.md) protocol in the Markdown string. To do this, use Apple’s Markdown extension syntax: `^[text](attribute1: value1, attribute2: value2, …)`.

When using attributes beyond those provided by the system, be sure to use initializers that take a `scope` parameter, and provide the scope that defines the custom attributes.

> 💡 **Tip**:  The [`AttributedString`](./attributedstring.md) initializers that take a `localized` parameter can also use Markdown syntax. These initializers allow you to use Markdown in your app’s strings files.

## Topics

### Initializing from Markdown Strings
- [init(markdown: String, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28markdown,options,baseurl%29-52n3u.md)
  Creates an attributed string from a Markdown-formatted string using the provided options.
- [init<S>(markdown: String, including: S.Type, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28markdown,including,options,baseurl%29-4m51b.md)
  Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope.
- [init<S>(markdown: String, including: KeyPath<AttributeScopes, S.Type>, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28markdown,including,options,baseurl%29-89e48.md)
  Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope that a key path identifies.
### Initializing from Markdown Data
- [init(markdown: Data, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28markdown,options,baseurl%29-2sg1o.md)
  Creates an attributed string from Markdown-formatted data using the provided options.
- [init<S>(markdown: Data, including: S.Type, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28markdown,including,options,baseurl%29-4co46.md)
  Creates an attributed string from Markdown-formatted data using the provided options and attribute scope.
- [init<S>(markdown: Data, including: KeyPath<AttributeScopes, S.Type>, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28markdown,including,options,baseurl%29-5nap7.md)
  Creates an attributed string from Markdown-formatted data using the provided options and attribute scope that a key path identifies.
### Initializing with Markdown from URL Contents
- [init(contentsOf: URL, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28contentsof,options,baseurl%29.md)
  Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data, using the provided options.
- [init<S>(contentsOf: URL, including: S.Type, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28contentsof,including,options,baseurl%29-1x6fz.md)
  Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data, using the provided options and attribute scope.
- [init<S>(contentsOf: URL, including: KeyPath<AttributeScopes, S.Type>, options: AttributedString.MarkdownParsingOptions, baseURL: URL?) throws](./attributedstring/init%28contentsof,including,options,baseurl%29-1fcpy.md)
  Creates an attributed string from the contents of a specified Markdown URL, using the provided options and attribute scope that a key path identifies.
### Specifying Markdown Parsing Options
- [AttributedString.MarkdownParsingOptions](./attributedstring/markdownparsingoptions.md)
  Options that affect the parsing of Markdown content into an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/instantiating-attributed-strings-with-markdown-syntax)*