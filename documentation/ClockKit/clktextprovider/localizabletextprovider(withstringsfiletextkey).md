# localizableTextProvider(withStringsFileTextKey:)

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Creates a localizable simple text provider using the strings file key for the text.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

## Declaration

```swift
class func localizableTextProvider(withStringsFileTextKey textKey: String) -> Self
```

```objc
+ (instancetype) localizableTextProviderWithStringsFileTextKey:(NSString *) textKey;
```

## Return Value

A text provider object built from the specified arguments.

## Discussion

Use this method to create a text provider that returns localized strings.

## Parameters

- `textKey`: The key for the desired text. This key must appear in the localized string files named `ckcomplication.strings` in the WatchKit extension target.

## See Also

### Creating Localized Text Providers
- [class func localizableTextProvider(withStringsFileTextKey: String, shortTextKey: String?) -> Self](./localizabletextprovider%28withstringsfiletextkey,shorttextkey%29.md)
  Creates a localizable simple text provider using strings file keys for both the regular text and the shorter fallback text.
- [class func localizableTextProvider(withStringsFileFormatKey: String, textProviders: [CLKTextProvider]) -> Self](./localizabletextprovider%28withstringsfileformatkey,textproviders%29.md)
  Creates a localizable text provider with a strings file key that resolves to a format string, and with text providers for the replacement arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktextprovider/localizabletextprovider(withstringsfiletextkey:))*