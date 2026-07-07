# init(excludeScheme:domain:path:query:excludeFragment:excludeIntermediates:caseSensitive:)

**Framework**: Network Extension  
**Kind**: init

Creates a new parsing configuration with the default values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
init(excludeScheme: Bool = true, domain: NEURLFilterManager.ParsingConfiguration.DomainOptions = DomainOptions(), path: NEURLFilterManager.ParsingConfiguration.PathOptions = PathOptions(), query: NEURLFilterManager.ParsingConfiguration.QueryOptions = QueryOptions(), excludeFragment: Bool = false, excludeIntermediates: Bool = false, caseSensitive: Bool = false)
```

#### Discussion

The configuration’s default behavior is as follows:

- Parsing includes domain, path, query and fragment, and excludes scheme and the `www` subdomain.
- Parsing is case-insensitive.
- Parsing enumerates all possible sub-URL combinations.

## Parameters

- `excludeScheme`: A Boolean value that indicates whether parsing should exclude the URL scheme. Defaults to `true`.
- `domain`: Parsing options for the URL domain component.
- `path`: Parsing options for the URL path component.
- `query`: Parsing options for the URL query component.
- `excludeFragment`: A Boolean value that indicates whether parsing should exclude the URL fragment. Defaults to `false`.
- `excludeIntermediates`: A Boolean value that indicates whether parsing should exclude intermediate pattern combinations. Defaults to `false`.
- `caseSensitive`: A Boolean value that indicates whether parsing should be case-sensitive. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/init(excludescheme:domain:path:query:excludefragment:excludeintermediates:casesensitive:))*