# localizableTextProvider(withStringsFileTextKey:shortTextKey:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Creates a localizable simple text provider using strings file keys for both the regular text and the shorter fallback text.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

## Declaration

```swift
class func localizableTextProvider(withStringsFileTextKey textKey: String, shortTextKey: String?) -> Self
```

```objc
+ (instancetype) localizableTextProviderWithStringsFileTextKey:(NSString *) textKey shortTextKey:(NSString *) shortTextKey;
```

#### Return Value

A text provider object built from the specified arguments.

#### Discussion

Use this method to create a text provider that returns localized strings with a shorter fallback string.

## Parameters

- `textKey`: The key for the desired text. This key must appear in the localized string files named `ckcomplication.strings` in the WatchKit extension target.
- `shortTextKey`: The key for the desired fallback text. This key must appear in the localized string files named `ckcomplication.strings` in the WatchKit extension target.

## See Also

### Creating Localized Text Providers
- [class func localizableTextProvider(withStringsFileTextKey: String) -> Self](./localizabletextprovider%28withstringsfiletextkey%29.md)
  Creates a localizable simple text provider using the strings file key for the text.
- [class func localizableTextProvider(withStringsFileFormatKey: String, textProviders: [CLKTextProvider]) -> Self](./localizabletextprovider%28withstringsfileformatkey,textproviders%29.md)
  Creates a localizable text provider with a strings file key that resolves to a format string, and with text providers for the replacement arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider/localizabletextprovider(withstringsfiletextkey:shorttextkey:))*