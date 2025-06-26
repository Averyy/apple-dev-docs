# supportedLocale(equivalentTo:)

**Framework**: Speech  
**Kind**: method  
**Required**: Yes

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

Use this method to determine which of this module’s supported locales is equivalent to an arbitrary locale such as `Locale.current`. Use this method instead of `supportedLocales.contains(_:)`; two locales may be equivalent but not equal, and `contains(_:)` uses equality rather than equivalence.

## Parameters

- `locale`: An arbitrary locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/localedependentspeechmodule/supportedlocale(equivalentto:))*