# supportedLocale(equivalentTo:)

**Framework**: Speech  
**Kind**: method

A locale from the module’s supported locales equivalent to the given locale.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func supportedLocale(equivalentTo locale: Locale) async -> Locale?
```

#### Return Value

A locale in the supported locales list, or `nil` if there is no equivalent locale in that list.

#### Discussion

Use this method to determine which of this module’s supported locales is equivalent to an arbitrary locale such as `Locale.current`.

If there is no exact equivalent, this method will return a near-equivalent: a supported (and by preference already-installed) locale that shares the same `Locale.LanguageCode` value but has a different `Locale.Region` value. This may result in an unexpected transcription, such as between “color” and “colour”.

> 💡 **Tip**: If you use this method, your application should ideally still provide a way for the user to correct the locale by selecting from the supported locales list.

## Parameters

- `locale`: An arbitrary locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/supportedlocale(equivalentto:))*