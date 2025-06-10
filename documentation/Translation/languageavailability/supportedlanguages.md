# supportedLanguages

**Framework**: Translation  
**Kind**: property

A list of translation languages the framework supports.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
var supportedLanguages: [Locale.Language] { get async }
```

#### Return Value

An array of languages the framework supports.

#### Discussion

A language must download before it can be used in a translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/supportedlanguages)*