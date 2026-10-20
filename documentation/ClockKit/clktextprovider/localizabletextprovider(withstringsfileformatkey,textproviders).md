# localizableTextProvider(withStringsFileFormatKey:textProviders:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Creates a localizable text provider with a strings file key that resolves to a format string, and with text providers for the replacement arguments.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

## Declaration

```swift
class func localizableTextProvider(withStringsFileFormatKey formatKey: String, textProviders: [CLKTextProvider]) -> Self
```

```objc
+ (instancetype) localizableTextProviderWithStringsFileFormatKey:(NSString *) formatKey textProviders:(NSArray<CLKTextProvider *> *) textProviders;
```

#### Return Value

A text provider object built from the specified arguments.

#### Discussion

Use this method to create a compound text provider using a format string, with other text providers to provide the replacement arguments.

## Parameters

- `formatKey`: The key for the localized format string. This key must appear in the localized string files named `ckcomplication.strings` in the WatchKit extension target.

  Since the format string’s replacement arguments come from other text providers, the only allowable format specifiers are `%@` and variants (for example, reordering specifiers like `%1@` are also supported).
- `textProviders`: The text providers that produce the format string’s replacement arguments.

## See Also

### Creating Localized Text Providers
- [class func localizableTextProvider(withStringsFileTextKey: String) -> Self](./localizabletextprovider%28withstringsfiletextkey%29.md)
  Creates a localizable simple text provider using the strings file key for the text.
- [class func localizableTextProvider(withStringsFileTextKey: String, shortTextKey: String?) -> Self](./localizabletextprovider%28withstringsfiletextkey,shorttextkey%29.md)
  Creates a localizable simple text provider using strings file keys for both the regular text and the shorter fallback text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider/localizabletextprovider(withstringsfileformatkey:textproviders:))*