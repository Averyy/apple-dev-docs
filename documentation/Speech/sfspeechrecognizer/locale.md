# locale

**Framework**: Speech  
**Kind**: property

The locale of the speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var locale: Locale { get }
```

#### Discussion

The locale of the speech recognizer is an [`NSLocale`](https://developer.apple.com/documentation/Foundation/NSLocale) object. The default value of this property is the system locale (that is, [`system`](https://developer.apple.com/documentation/foundation/nslocale/1407691-system)).

## See Also

- [class func supportedLocales() -> Set<Locale>](sfspeechrecognizer/supportedlocales.md)
  Returns the set of locales that are supported by the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/locale)*