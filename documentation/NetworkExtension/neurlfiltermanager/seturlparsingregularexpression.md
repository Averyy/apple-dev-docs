# setURLParsingRegularExpression(_:)

**Framework**: Network Extension  
**Kind**: method

Sets a regular expression for use in URL parsing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
func setURLParsingRegularExpression(_ pattern: String?) throws
```

#### Discussion

Setting a regular expression allows you to perform custom URL parsing patterns beyond the standard parsing options. The filter uses the regular expression to parse the URL before matching against the specified data set.

Calling this method validates the `pattern` you provide for the regular expression. In your regular expression, use the standard name captured group syntax. For example, `"https?://(?<host>[^/]+)"` captures the domain by using the group name `host`. You can use whatever custom labels you want for group names, but they are limited to ASCII alphanumeric characters.

The result is a single string that uses the space character for a delimiter between each name-value pair, such as:

```not specified
<group-1-name>=<group-1-value> <group-2-name>=<group-2-value> <group-3-name>=...
```

Providing a `pattern` without a named capture group throws an error. If you provide a regular expression that uses other types of captured groups, only the named captured groups appear in the result.

Setting a regular expression causes the [`urlParsingConfiguration`](neurlfiltermanager/urlparsingconfiguration.md) parameter to have no effect. You can read the current value of the regular expression with the [`urlParsingRegularExpression`](neurlfiltermanager/urlparsingregularexpression.md) property.

URL parsing with a regular expression is case insensitive.

## See Also

- [var urlParsingConfiguration: NEURLFilterManager.ParsingConfiguration](neurlfiltermanager/urlparsingconfiguration.md)
  A property to configure the filter’s parser behavior.
- [NEURLFilterManager.ParsingConfiguration](neurlfiltermanager/parsingconfiguration.md)
  A type to configure the filter’s parser behavior.
- [var urlParsingRegularExpression: String?](neurlfiltermanager/urlparsingregularexpression.md)
  A regular expression used for advanced URL parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/seturlparsingregularexpression(_:))*