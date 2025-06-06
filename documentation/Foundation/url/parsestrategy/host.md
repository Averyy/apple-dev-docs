# host(_:)

**Framework**: Foundation  
**Kind**: method

Modifies a parse strategy to parse a URL’s host component in accordance with the provided behavior.

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
func host(_ strategy: URL.ParseStrategy.ComponentParseStrategy<String> = .required) -> URL.ParseStrategy
```

#### Return Value

A modified [`URL.ParseStrategy`](url/parsestrategy.md) that incorporates the specified behavior.

## Parameters

- `strategy`: A strategy for parsing the host component.

## See Also

- [func scheme(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](url/parsestrategy/scheme(_:).md)
  Modifies a parse strategy to parse a URL’s scheme component in accordance with the provided behavior.
- [func user(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](url/parsestrategy/user(_:).md)
  Modifies a parse strategy to parse a URL’s user component in accordance with the provided behavior.
- [func password(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](url/parsestrategy/password(_:).md)
  Modifies a parse strategy to parse a URL’s password component in accordance with the provided behavior.
- [func port(URL.ParseStrategy.ComponentParseStrategy<Int>) -> URL.ParseStrategy](url/parsestrategy/port(_:).md)
  Modifies a parse strategy to parse a URL’s port component in accordance with the provided behavior.
- [func path(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](url/parsestrategy/path(_:).md)
  Modifies a parse strategy to parse a URL’s path component in accordance with the provided behavior.
- [func query(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](url/parsestrategy/query(_:).md)
  Modifies a parse strategy to parse a URL’s query component in accordance with the provided behavior.
- [func fragment(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](url/parsestrategy/fragment(_:).md)
  Modifies a parse strategy to parse a URL’s fragment component in accordance with the provided behavior.
- [URL.ParseStrategy.ComponentParseStrategy](url/parsestrategy/componentparsestrategy.md)
  The strategy used to parse one component of a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/parsestrategy/host(_:))*