# URL.ParseStrategy

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A parse strategy for creating URLs from formatted strings.

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
struct ParseStrategy
```

#### Overview

Create an explicit [`URL.ParseStrategy`](./parsestrategy.md) to parse multiple strings according to the same parse strategy. The following example creates a customized strategy, then applies it to multiple URL candidate strings.

```swift
let strategy = URL.ParseStrategy(
    scheme: .defaultValue("https"),
    user: .optional,
    password: .optional,
    host: .required,
    port: .optional,
    path: .required,
    query: .required,
    fragment: .optional)
let urlStrings = [
    "example.com?key1=value1", // no scheme or path
    "https://example.com?key2=value2", // no path
    "https://example.com", // no query
    "https://example.com/path?key4=value4", // complete
    "//example.com/path?key5=value5" // complete except for default-able scheme
]
let urls = urlStrings.map { try? strategy.parse($0) } // [nil, nil, nil, Optional(https://example.com/path?key4=value4), Optional(https://example.com/path?key5=value5)]
```

You don’t need to instantiate a parse strategy instance to parse a single string. Instead, use the URL initializer [`init(_:strategy:)`](./init%28_,strategy%29.md), passing in a string to parse and a customized strategy, typically created with one of the static accessors. The following example parses a URL string, with a custom strategy that provides a default value for the port component if the source string doesn’t specify one.

```swift
let urlString = "https://internal.example.com/path/to/endpoint?key=value"
let url = try? URL(urlString, strategy: .url
    .port(.defaultValue(8080))) // https://internal.example.com:8080/path/to/endpoint?key=value

```

## Topics

### Creating a URL parse strategy
- [init(scheme: URL.ParseStrategy.ComponentParseStrategy<String>, user: URL.ParseStrategy.ComponentParseStrategy<String>, password: URL.ParseStrategy.ComponentParseStrategy<String>, host: URL.ParseStrategy.ComponentParseStrategy<String>, port: URL.ParseStrategy.ComponentParseStrategy<Int>, path: URL.ParseStrategy.ComponentParseStrategy<String>, query: URL.ParseStrategy.ComponentParseStrategy<String>, fragment: URL.ParseStrategy.ComponentParseStrategy<String>)](./parsestrategy/init%28scheme,user,password,host,port,path,query,fragment%29.md)
  Creates a URL parse strategy with the specified component-parsing behaviors.
- [URL.ParseStrategy.ComponentParseStrategy](./parsestrategy/componentparsestrategy.md)
  The strategy used to parse one component of a URL.
### Customizing strategy behavior
- [func scheme(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./parsestrategy/scheme%28_%29.md)
  Modifies a parse strategy to parse a URL’s scheme component in accordance with the provided behavior.
- [func user(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./parsestrategy/user%28_%29.md)
  Modifies a parse strategy to parse a URL’s user component in accordance with the provided behavior.
- [func password(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./parsestrategy/password%28_%29.md)
  Modifies a parse strategy to parse a URL’s password component in accordance with the provided behavior.
- [func host(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./parsestrategy/host%28_%29.md)
  Modifies a parse strategy to parse a URL’s host component in accordance with the provided behavior.
- [func port(URL.ParseStrategy.ComponentParseStrategy<Int>) -> URL.ParseStrategy](./parsestrategy/port%28_%29.md)
  Modifies a parse strategy to parse a URL’s port component in accordance with the provided behavior.
- [func path(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./parsestrategy/path%28_%29.md)
  Modifies a parse strategy to parse a URL’s path component in accordance with the provided behavior.
- [func query(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./parsestrategy/query%28_%29.md)
  Modifies a parse strategy to parse a URL’s query component in accordance with the provided behavior.
- [func fragment(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./parsestrategy/fragment%28_%29.md)
  Modifies a parse strategy to parse a URL’s fragment component in accordance with the provided behavior.
- [URL.ParseStrategy.ComponentParseStrategy](./parsestrategy/componentparsestrategy.md)
  The strategy used to parse one component of a URL.
### Parsing strings
- [func parse(String) throws -> URL](./parsestrategy/parse%28_%29.md)
  Parses a URL string in accordance with this strategy and returns the parsed value.
### Locating URLs with regular expressions
- [func consuming(String, startingAt: String.Index, in: Range<String.Index>) throws -> (upperBound: String.Index, output: URL)?](./parsestrategy/consuming%28_,startingat,in%29.md)
  Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.
### Supporting Types
- [URL.ParseStrategy.RegexOutput](./parsestrategy/regexoutput.md)
  The type returned when capturing matching substrings with this strategy.
### Default Implementations
- [CustomConsumingRegexComponent Implementations](./parsestrategy/customconsumingregexcomponent-implementations.md)
- [ParseStrategy Implementations](./parsestrategy/parsestrategy-implementations.md)
- [RegexComponent Implementations](./parsestrategy/regexcomponent-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomConsumingRegexComponent](../../Swift/customconsumingregexcomponent.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [ParseStrategy](../parsestrategy.md)
- [RegexComponent](../../Swift/regexcomponent.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Parsing URLs
- [var parseStrategy: URL.ParseStrategy](./formatstyle/parsestrategy.md)
  The parse strategy used by this format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/parsestrategy)*