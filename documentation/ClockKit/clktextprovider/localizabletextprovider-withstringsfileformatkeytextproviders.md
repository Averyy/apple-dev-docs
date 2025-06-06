# localizableTextProvider(withStringsFileFormatKey:textProviders:)

**Framework**: ClockKit  
**Kind**: method

Creates a localizable text provider with a strings file key that resolves to a format string, and with text providers for the replacement arguments.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders: [CLKTextProvider]) -> Self
```

#### Return Value

A text provider object built from the specified arguments.

#### Discussion

Use this method to create a compound text provider using a format string, with other text providers to provide the replacement arguments.

## Parameters

- `formatKey`: Since the format string’s replacement arguments come from other text providers, the only allowable format specifiers are   and variants (for example, reordering specifiers like   are also supported).
- `textProviders`: The text providers that produce the format string’s replacement arguments.

## See Also

- [class func localizableTextProvider(withStringsFileTextKey: String) -> Self](clktextprovider/localizabletextprovider(withstringsfiletextkey:).md)
  Creates a localizable simple text provider using the strings file key for the text.
- [class func localizableTextProvider(withStringsFileTextKey: String, shortTextKey: String?) -> Self](clktextprovider/localizabletextprovider(withstringsfiletextkey:shorttextkey:).md)
  Creates a localizable simple text provider using strings file keys for both the regular text and the shorter fallback text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider/localizabletextprovider(withstringsfileformatkey:textproviders:))*