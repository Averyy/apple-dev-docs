# NEURLFilterManager.ParsingConfiguration.DomainOptions

**Framework**: Network Extension  
**Kind**: struct

A type that represents options for parsing the URL domain component.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct DomainOptions
```

## Topics

### Creating a domain options instance
- [init(excluded: Bool, stripWWW: Bool, levels: UInt, enumerateHierarchy: Bool)](neurlfiltermanager/parsingconfiguration/domainoptions/init(excluded:stripwww:levels:enumeratehierarchy:).md)
  Creates a new domain options configuration with default values.
### Working with domain options
- [var excluded: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/excluded.md)
  A Boolean value that indicates whether to exclude the domain component from URL parsing.
- [var stripWWW: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/stripwww.md)
  A Boolean value that indicates whether to strip the `www` subdomain when parsing.
- [var levels: UInt](neurlfiltermanager/parsingconfiguration/domainoptions/levels.md)
  The number of domain levels to preserve when parsing.
- [var enumerateHierarchy: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/enumeratehierarchy.md)
  A Boolean value that indicates whether the parser walks the domain hierarchy for matching.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var excludeScheme: Bool](neurlfiltermanager/parsingconfiguration/excludescheme.md)
  A Boolean value that indicates whether parsing should exclude the URL scheme.
- [var domain: NEURLFilterManager.ParsingConfiguration.DomainOptions](neurlfiltermanager/parsingconfiguration/domain.md)
  Parsing options for the URL domain component.
- [var path: NEURLFilterManager.ParsingConfiguration.PathOptions](neurlfiltermanager/parsingconfiguration/path.md)
  Parsing options for the URL path component.
- [NEURLFilterManager.ParsingConfiguration.PathOptions](neurlfiltermanager/parsingconfiguration/pathoptions.md)
  A type that represents options for parsing the URL path component.
- [var query: NEURLFilterManager.ParsingConfiguration.QueryOptions](neurlfiltermanager/parsingconfiguration/query.md)
  Parsing options for the URL query component.
- [NEURLFilterManager.ParsingConfiguration.QueryOptions](neurlfiltermanager/parsingconfiguration/queryoptions.md)
  A type that represents options for parsing the URL query component.
- [var excludeFragment: Bool](neurlfiltermanager/parsingconfiguration/excludefragment.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var excludeIntermediates: Bool](neurlfiltermanager/parsingconfiguration/excludeintermediates.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var caseSensitive: Bool](neurlfiltermanager/parsingconfiguration/casesensitive.md)
  A Boolean value that indicates whether parsing should be case-sensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/domainoptions)*