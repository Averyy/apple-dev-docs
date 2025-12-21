# supportedLocale(equivalentTo:)

**Framework**: Speech  
**Kind**: method  
**Required**: Yes

A locale from the module’s supported locales equivalent to the given locale.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

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

## See Also

- [static var supportedLocales: [Locale]](localedependentspeechmodule/supportedlocales.md)
  The set of all possible asset locales that the module supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/localedependentspeechmodule/supportedlocale(equivalentto:))*