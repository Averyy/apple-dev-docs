# fragment(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies a parse strategy to parse a URL’s fragment component in accordance with the provided behavior.

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
func fragment(_ strategy: URL.ParseStrategy.ComponentParseStrategy<String> = .optional) -> URL.ParseStrategy
```

#### Return Value

A modified [`URL.ParseStrategy`](../parsestrategy.md) that incorporates the specified behavior.

## Parameters

- `strategy`: A strategy for parsing the fragment component.

## See Also

### Customizing strategy behavior
- [func scheme(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./scheme%28_%29.md)
  Modifies a parse strategy to parse a URL’s scheme component in accordance with the provided behavior.
- [func user(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./user%28_%29.md)
  Modifies a parse strategy to parse a URL’s user component in accordance with the provided behavior.
- [func password(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./password%28_%29.md)
  Modifies a parse strategy to parse a URL’s password component in accordance with the provided behavior.
- [func host(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./host%28_%29.md)
  Modifies a parse strategy to parse a URL’s host component in accordance with the provided behavior.
- [func port(URL.ParseStrategy.ComponentParseStrategy<Int>) -> URL.ParseStrategy](./port%28_%29.md)
  Modifies a parse strategy to parse a URL’s port component in accordance with the provided behavior.
- [func path(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./path%28_%29.md)
  Modifies a parse strategy to parse a URL’s path component in accordance with the provided behavior.
- [func query(URL.ParseStrategy.ComponentParseStrategy<String>) -> URL.ParseStrategy](./query%28_%29.md)
  Modifies a parse strategy to parse a URL’s query component in accordance with the provided behavior.
- [URL.ParseStrategy.ComponentParseStrategy](./componentparsestrategy.md)
  The strategy used to parse one component of a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/parsestrategy/fragment(_:))*