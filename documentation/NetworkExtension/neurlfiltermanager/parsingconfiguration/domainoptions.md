# NEURLFilterManager.ParsingConfiguration.DomainOptions

**Framework**: Network Extension  
**Kind**: struct  
**Role**: Structure

A type that represents options for parsing the URL domain component.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct DomainOptions
```

## Topics

### Creating a domain options instance
- [init(excluded: Bool, stripWWW: Bool, levels: UInt, enumerateHierarchy: Bool)](./domainoptions/init%28excluded,stripwww,levels,enumeratehierarchy%29.md)
  Creates a new domain options configuration with default values.
### Working with domain options
- [var excluded: Bool](./domainoptions/excluded.md)
  A Boolean value that indicates whether to exclude the domain component from URL parsing.
- [var stripWWW: Bool](./domainoptions/stripwww.md)
  A Boolean value that indicates whether to strip the `www` subdomain when parsing.
- [var levels: UInt](./domainoptions/levels.md)
  The number of domain levels to preserve when parsing.
- [var enumerateHierarchy: Bool](./domainoptions/enumeratehierarchy.md)
  A Boolean value that indicates whether the parser walks the domain hierarchy for matching.

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
- [var path: NEURLFilterManager.ParsingConfiguration.PathOptions](./path.md)
  Parsing options for the URL path component.
- [NEURLFilterManager.ParsingConfiguration.PathOptions](./pathoptions.md)
  A type that represents options for parsing the URL path component.
- [var query: NEURLFilterManager.ParsingConfiguration.QueryOptions](./query.md)
  Parsing options for the URL query component.
- [NEURLFilterManager.ParsingConfiguration.QueryOptions](./queryoptions.md)
  A type that represents options for parsing the URL query component.
- [var excludeFragment: Bool](./excludefragment.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var excludeIntermediates: Bool](./excludeintermediates.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var caseSensitive: Bool](./casesensitive.md)
  A Boolean value that indicates whether parsing should be case-sensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/domainoptions)*