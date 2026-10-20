# NEURLFilterManager.ParsingConfiguration.QueryOptions

**Framework**: Network Extension  
**Kind**: struct  
**Role**: Structure

A type that represents options for parsing the URL query component.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct QueryOptions
```

## Topics

### Creating a query options instance
- [init(excluded: Bool, parameters: [String]?)](./queryoptions/init%28excluded,parameters%29.md)
  Creates a new query options configuration with default values.
### Working with query options
- [var excluded: Bool](./queryoptions/excluded.md)
  A Boolean value that indicates whether to exclude the query component from URL parsing.
- [var parameters: [String]?](./queryoptions/parameters.md)
  An array of parameter names to extract.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Working with configuration options
- [var excludeScheme: Bool](./excludescheme.md)
  A Boolean value that indicates whether parsing should exclude the URL scheme.
- [var domain: NEURLFilterManager.ParsingConfiguration.DomainOptions](./domain.md)
  Parsing options for the URL domain component.
- [NEURLFilterManager.ParsingConfiguration.DomainOptions](./domainoptions.md)
  A type that represents options for parsing the URL domain component.
- [var path: NEURLFilterManager.ParsingConfiguration.PathOptions](./path.md)
  Parsing options for the URL path component.
- [NEURLFilterManager.ParsingConfiguration.PathOptions](./pathoptions.md)
  A type that represents options for parsing the URL path component.
- [var query: NEURLFilterManager.ParsingConfiguration.QueryOptions](./query.md)
  Parsing options for the URL query component.
- [var excludeFragment: Bool](./excludefragment.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var excludeIntermediates: Bool](./excludeintermediates.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var caseSensitive: Bool](./casesensitive.md)
  A Boolean value that indicates whether parsing should be case-sensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/queryoptions)*