# NEURLFilterManager.ParsingConfiguration

**Framework**: Network Extension  
**Kind**: struct  
**Role**: Structure

A type to configure the filter’s parser behavior.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct ParsingConfiguration
```

#### Overview

Use this property to control which URL components to exclude, and to customize parsing behavior during sub-URL enumeration. By default, filtering is case-insensitive and includes all components except the scheme and the `www` subdomain. The filter enumerates all possible sub-URL combinations by walking up both the domain hierarchy and path hierarchy, including intermediate results.

For example, given a domain of `a.b.c.com`, walking the domain hierarchy includes `a.b.c.com`, `b.c.com` and `c.com`. For a path of `/a/b/c`, walking the path hierarchy includes `/a`, `/a/b`, and `/a/b/c`. This also allows for intermediate pattern combinations. For example, `example.com/a/b/c?id=123` includes `example.com`, `example.com/a`, `example.com/a/b`, `example.com/a/b/c`, and `example.com/a/b/c?id=123`.

## Topics

### Creating a configuration
- [init(excludeScheme: Bool, domain: NEURLFilterManager.ParsingConfiguration.DomainOptions, path: NEURLFilterManager.ParsingConfiguration.PathOptions, query: NEURLFilterManager.ParsingConfiguration.QueryOptions, excludeFragment: Bool, excludeIntermediates: Bool, caseSensitive: Bool)](./parsingconfiguration/init%28excludescheme,domain,path,query,excludefragment,excludeintermediates,casesensitive%29.md)
  Creates a new parsing configuration with the default values.
### Working with configuration options
- [var excludeScheme: Bool](./parsingconfiguration/excludescheme.md)
  A Boolean value that indicates whether parsing should exclude the URL scheme.
- [var domain: NEURLFilterManager.ParsingConfiguration.DomainOptions](./parsingconfiguration/domain.md)
  Parsing options for the URL domain component.
- [NEURLFilterManager.ParsingConfiguration.DomainOptions](./parsingconfiguration/domainoptions.md)
  A type that represents options for parsing the URL domain component.
- [var path: NEURLFilterManager.ParsingConfiguration.PathOptions](./parsingconfiguration/path.md)
  Parsing options for the URL path component.
- [NEURLFilterManager.ParsingConfiguration.PathOptions](./parsingconfiguration/pathoptions.md)
  A type that represents options for parsing the URL path component.
- [var query: NEURLFilterManager.ParsingConfiguration.QueryOptions](./parsingconfiguration/query.md)
  Parsing options for the URL query component.
- [NEURLFilterManager.ParsingConfiguration.QueryOptions](./parsingconfiguration/queryoptions.md)
  A type that represents options for parsing the URL query component.
- [var excludeFragment: Bool](./parsingconfiguration/excludefragment.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var excludeIntermediates: Bool](./parsingconfiguration/excludeintermediates.md)
  A Boolean value that indicates whether parsing should exclude the URL fragment.
- [var caseSensitive: Bool](./parsingconfiguration/casesensitive.md)
  A Boolean value that indicates whether parsing should be case-sensitive.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing filter parsing behavior
- [var urlParsingConfiguration: NEURLFilterManager.ParsingConfiguration](./urlparsingconfiguration.md)
  A property to configure the filter’s parser behavior.
- [var urlParsingRegularExpression: String?](./urlparsingregularexpression.md)
  A regular expression used for advanced URL parsing.
- [func setURLParsingRegularExpression(String?) throws](./seturlparsingregularexpression%28_%29.md)
  Sets a regular expression for use in URL parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration)*