# urlParsingRegularExpression

**Framework**: Network Extension  
**Kind**: property

A regular expression used for advanced URL parsing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var urlParsingRegularExpression: String? { get }
```

#### Discussion

This property is read-only. To set a regular expression for use in parsing, call [`setURLParsingRegularExpression(_:)`](neurlfiltermanager/seturlparsingregularexpression(_:).md), which validates the pattern.

Setting a regular expression allows you to perform custom URL parsing patterns beyond the standard parsing options. The filter uses the regular expression to parse the URL before matching against the specified data set.

URL parsing with a regular expression is case insensitive.

## See Also

- [var urlParsingConfiguration: NEURLFilterManager.ParsingConfiguration](neurlfiltermanager/urlparsingconfiguration.md)
  A property to configure the filter’s parser behavior.
- [NEURLFilterManager.ParsingConfiguration](neurlfiltermanager/parsingconfiguration.md)
  A type to configure the filter’s parser behavior.
- [func setURLParsingRegularExpression(String?) throws](neurlfiltermanager/seturlparsingregularexpression(_:).md)
  Sets a regular expression for use in URL parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/urlparsingregularexpression)*