# urlParsingConfiguration

**Framework**: Network Extension  
**Kind**: property

A property to configure the filter’s parser behavior.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var urlParsingConfiguration: NEURLFilterManager.ParsingConfiguration { get set }
```

#### Discussion

Use this property to control which URL components to exclude, and to customize parsing behavior during sub-URL enumeration. This determines how the filter parses URLs which sub-URLs it generates for matching against the filter data set.

For any excluded component – domain, path, query, or fragment –  the filter substitutes `"%*"` in place as a placeholder. By contrast, if you strip the domain or `www` subdomain, they’re removed entirely without a placeholder, since URL matching doesn’t typically require them.

As an example, consider the URL `https://www.example.com/a/b/c?id=123#fragment` and a configuration set as follows:

```swift
var config = manager.urlParsingConfiguration
config.excludeScheme = true
config.domain.stripWWW = true
config.path.excluded = true
manager.urlParsingConfiguration = config
```

The parsing result is `example.com/%*?id=123#fragment`, where `"%*"` acts as the placeholder for the excluded path component. The presence of a placeholder indicates the original URL contained that component, but the parsing configuration excluded it.

If the filter manager sets [`urlParsingRegularExpression`](neurlfiltermanager/urlparsingregularexpression.md), this configuration has no effect.

## See Also

- [NEURLFilterManager.ParsingConfiguration](neurlfiltermanager/parsingconfiguration.md)
  A type to configure the filter’s parser behavior.
- [var urlParsingRegularExpression: String?](neurlfiltermanager/urlparsingregularexpression.md)
  A regular expression used for advanced URL parsing.
- [func setURLParsingRegularExpression(String?) throws](neurlfiltermanager/seturlparsingregularexpression(_:).md)
  Sets a regular expression for use in URL parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/urlparsingconfiguration)*