# init(scheme:user:password:host:port:path:query:fragment:)

**Framework**: Foundation  
**Kind**: init

Creates a URL parse strategy with the specified component-parsing behaviors.

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
init(scheme: URL.ParseStrategy.ComponentParseStrategy<String> = .required, user: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, password: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, host: URL.ParseStrategy.ComponentParseStrategy<String> = .required, port: URL.ParseStrategy.ComponentParseStrategy<Int> = .optional, path: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, query: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, fragment: URL.ParseStrategy.ComponentParseStrategy<String> = .optional)
```

## Parameters

- `scheme`: A strategy for parsing the scheme component.
- `user`: A strategy for parsing the user component.
- `password`: A strategy for parsing the password component.
- `host`: A strategy for parsing the host component.
- `port`: A strategy for parsing the port component.
- `path`: A strategy for parsing the path component.
- `query`: A strategy for parsing the query component.
- `fragment`: A strategy for parsing the fragment component.

## See Also

- [URL.ParseStrategy.ComponentParseStrategy](url/parsestrategy/componentparsestrategy.md)
  The strategy used to parse one component of a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/parsestrategy/init(scheme:user:password:host:port:path:query:fragment:))*