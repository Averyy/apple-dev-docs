# NEURLFilterManager.ParsingConfiguration.QueryOptions

**Framework**: Network Extension  
**Kind**: struct

A type that represents options for parsing the URL query component.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct QueryOptions
```

## Topics

### Creating a query options instance
- [init(excluded: Bool, parameters: [String]?)](neurlfiltermanager/parsingconfiguration/queryoptions/init(excluded:parameters:).md)
  Creates a new query options configuration with default values.
### Working with query options
- [var excluded: Bool](neurlfiltermanager/parsingconfiguration/queryoptions/excluded.md)
  A Boolean value that indicates whether to exclude the query component from URL parsing.
- [var parameters: [String]?](neurlfiltermanager/parsingconfiguration/queryoptions/parameters.md)
  An array of parameter names to extract.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var excludeScheme: Bool](neurlfiltermanager/parsingconfiguration/excludescheme.md)
  A Boolean value that indicates whether parsing should exclude the URL scheme.
- [var domain: NEURLFilterManager.ParsingConfiguration.DomainOptions](neurlfiltermanager/parsingconfiguration/domain.md)
  Parsing options for the URL domain component.
- [NEURLFilterManager.ParsingConfiguration.DomainOptions](neurlfiltermanager/parsingconfiguration/domainoptions.md)
  A type that represents options for parsing the URL domain component.
- [var path: NEURLFilterManager.ParsingConfiguration.PathOptions](neurlfiltermanager/parsingconfiguration/path.md)
  Parsing options for the URL path component.
- [NEURLFilterManager.ParsingConfiguration.PathOptions](neurlfiltermanager/parsingconfiguration/pathoptions.md)
  A type that represents options for parsing the URL path component.
- [var query: NEURLFilterManager.ParsingConfiguration.QueryOptions](neurlfiltermanager/parsingconfiguration/query.md)
  Parsing options for the URL query component.
- [var excludeFragment: Bool](neurlfiltermanager/parsingconfiguration/excludefragment.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var excludeIntermediates: Bool](neurlfiltermanager/parsingconfiguration/excludeintermediates.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var caseSensitive: Bool](neurlfiltermanager/parsingconfiguration/casesensitive.md)
  A Boolean value that indicates whether parsing should be case-sensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/queryoptions)*