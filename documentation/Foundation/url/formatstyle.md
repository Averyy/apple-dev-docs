# URL.FormatStyle

**Framework**: Foundation  
**Kind**: struct

A structure that converts between URL instances and their textual representations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct FormatStyle
```

#### Overview

Instances of [`URL.FormatStyle`](url/formatstyle.md) create localized, human-readable text from [`URL`](url.md) instances and parse string representations of URLs into instances of [`URL`](url.md).

##### Formatting Urls

Use the [`formatted()`](url/formatted().md) method to create a string representation of a URL using the default [`URL.FormatStyle`](url/formatstyle.md) configuration. As seen in the following example, the default style creates a string with the scheme, host, and path, but not the port or query.

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted() // "https://www.example.com/path/to/endpoint"
```

You can specify a format style by providing an argument to the `format(_:)` method. The following example uses the previous URL, but preserves only the host and path.

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let style = URL.FormatStyle(scheme: .never,
                            user: .never,
                            password: .never,
                            host: .always,
                            port: .never,
                            path: .always,
                            query: .never,
                            fragment: .never)
let formatted = style.format(url) // "www.example.com/path/to/endpoint"
```

Instantiate a style when you want to format multiple URL instances with the same style. For one-time access to a default style, you can use the static accessor [`url`](formatstyle/url.md) at call points that expect the [`URL.FormatStyle`](url/formatstyle.md) type, such as the `format(_:)` method. This means you can write the example above as follows:

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted(.url
    .scheme(.never)
    .host(.always)
    .port(.never)
    .path(.always)
    .query(.never)) // "www.example.com/path/to/endpoint"
```

This example works by taking the default style provided by [`url`](formatstyle/url.md), then customizing it with calls to the style modifiers in Customizing style behavior.

##### Parsing Urls

You can use [`URL.FormatStyle`](url/formatstyle.md) to parse strings into URL values. To do this, create a [`URL.ParseStrategy`](url/parsestrategy.md) from a format style, then call the strategy’s [`parse(_:)`](parsestrategy/parse(_:).md) method.

```swift
let style = URL.FormatStyle(scheme: .always,
                            user: .never,
                            password: .never,
                            host: .always,
                            port: .always,
                            path: .always,
                            query: .always,
                            fragment: .never)
let urlString = "https://www.example.com:8080/path/to/endpoint?key=value"
let url = try? style.parseStrategy.parse(urlString)
```

##### Matching Regular Expressions

Along with parsing URL values in strings, you can use the regular expression domain-specific language provided by Swift to match and capture URL substrings. The following example scans source input that’s expected to contain a timestamp, some whitespace, and a URL.

```swift
import RegexBuilder
let source = "7/31/2022, 5:15:12 AM  https://www.example.com/productList?query=slushie"
let matcher = Regex {
    One(.dateTime(date: .numeric,
                  time: .standard,
                  locale: Locale(identifier: "en_US"),
                  timeZone: TimeZone(identifier: "PST")!))
    OneOrMore(.horizontalWhitespace)
    Capture {
        One(.url(scheme: .required,
                 user: .optional,
                 password: .optional,
                 host: .required,
                 port: .defaultValue(8088),
                 path: .optional,
                 query: .optional,
                 fragment: .optional))
    }
}
guard let match = source.firstMatch(of: matcher) else { return }
let url = match.1 // url = https://www.example.com:8088/productList?query=slushie
```

## Topics

### Creating a URL format style
- [init(scheme: URL.FormatStyle.ComponentDisplayOption, user: URL.FormatStyle.ComponentDisplayOption, password: URL.FormatStyle.ComponentDisplayOption, host: URL.FormatStyle.HostDisplayOption, port: URL.FormatStyle.ComponentDisplayOption, path: URL.FormatStyle.ComponentDisplayOption, query: URL.FormatStyle.ComponentDisplayOption, fragment: URL.FormatStyle.ComponentDisplayOption)](url/formatstyle/init(scheme:user:password:host:port:path:query:fragment:).md)
  Creates a URL format style with the given display options.
- [URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption.md)
  A type that indicates whether a formatted URL should include a component.
- [URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption.md)
  A type that indicates whether a formatted URL should include the host component.
### Customizing style behavior
- [func scheme(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/scheme(_:).md)
  Modifies a format style to display a URL’s scheme component in accordance with the provided option.
- [func user(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/user(_:).md)
  Modifies a format style to display a URL’s user component in accordance with the provided option.
- [func password(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/password(_:).md)
  Modifies a format style to display a URL’s password component in accordance with the provided option.
- [func host(URL.FormatStyle.HostDisplayOption) -> URL.FormatStyle](url/formatstyle/host(_:).md)
  Modifies a format style to display a URL’s host component in accordance with the provided option.
- [URL.FormatStyle.HostDisplayOption](url/formatstyle/hostdisplayoption.md)
  A type that indicates whether a formatted URL should include the host component.
- [func port(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/port(_:).md)
  Modifies a format style to display a URL’s port component in accordance with the provided option.
- [func path(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/path(_:).md)
  Modifies a format style to display a URL’s path component in accordance with the provided option.
- [func query(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/query(_:).md)
  Modifies a format style to display a URL’s query component in accordance with the provided option.
- [func fragment(URL.FormatStyle.ComponentDisplayOption) -> URL.FormatStyle](url/formatstyle/fragment(_:).md)
  Modifies a format style to display a URL’s fragment component in accordance with the provided option.
- [URL.FormatStyle.ComponentDisplayOption](url/formatstyle/componentdisplayoption.md)
  A type that indicates whether a formatted URL should include a component.
### Parsing URLs
- [struct ParseStrategy](url/parsestrategy.md)
  A parse strategy for creating URLs from formatted strings.
### Enumerations
- [URL.FormatStyle.Component](url/formatstyle/component.md)
  An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [ParseableFormatStyle](parseableformatstyle.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Language Introspector](language-introspector.md)
  Converts data into human-readable text using formatters and locales.
- [protocol FormatStyle](formatstyle.md)
  A type that converts a given data type into a representation in another type, such as a string.
- [struct IntegerFormatStyle](integerformatstyle.md)
  A structure that converts between integer values and their textual representations.
- [struct FloatingPointFormatStyle](floatingpointformatstyle.md)
  A structure that converts between floating-point values and their textual representations.
- [Decimal.FormatStyle](decimal/formatstyle.md)
  A structure that converts between decimal values and their textual representations.
- [struct ListFormatStyle](listformatstyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [struct StringStyle](stringstyle.md)
- [struct FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md)
  The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](format-style-configurations.md)
  Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/formatstyle)*