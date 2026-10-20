# NEURLFilterManager.ParsingConfiguration.PathOptions

**Framework**: Network Extension  
**Kind**: struct  
**Role**: Structure

A type that represents options for parsing the URL path component.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct PathOptions
```

## Topics

### Creating a path options instance
- [init(excluded: Bool, segments: UInt, enumerateHierarchy: Bool)](./pathoptions/init%28excluded,segments,enumeratehierarchy%29.md)
  Creates a new path options configuration with default values.
### Working with path options
- [var excluded: Bool](./pathoptions/excluded.md)
  A Boolean value that indicates whether to exlude the path component from URL parsing.
- [var segments: UInt](./pathoptions/segments.md)
  The number of path levels to preserve when parsing.
- [var enumerateHierarchy: Bool](./pathoptions/enumeratehierarchy.md)
  A Boolean value that indicates whether the parser walks the path hierarchy for matching.

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

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/pathoptions)*