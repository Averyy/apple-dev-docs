# urlParsingRegularExpression

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A regular expression used for advanced URL parsing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var urlParsingRegularExpression: String? { get }
```

#### Discussion

This property is read-only. To set a regular expression for use in parsing, call [`setURLParsingRegularExpression(_:)`](./seturlparsingregularexpression%28_%29.md), which validates the pattern.

Setting a regular expression allows you to perform custom URL parsing patterns beyond the standard parsing options. The filter uses the regular expression to parse the URL before matching against the specified data set.

URL parsing with a regular expression is case insensitive.

## See Also

### Customizing filter parsing behavior
- [var urlParsingConfiguration: NEURLFilterManager.ParsingConfiguration](./urlparsingconfiguration.md)
  A property to configure the filter’s parser behavior.
- [NEURLFilterManager.ParsingConfiguration](./parsingconfiguration.md)
  A type to configure the filter’s parser behavior.
- [func setURLParsingRegularExpression(String?) throws](./seturlparsingregularexpression%28_%29.md)
  Sets a regular expression for use in URL parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/urlparsingregularexpression)*