# languages

**Framework**: ManagedAppDistribution  
**Kind**: property  
**Role**: Instance Property

The app’s supported languages.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

## Declaration

```swift
let languages: [Locale.Language]
```

#### Discussion

> 💡 **Tip**: Use `Locale.localizedString(forLanguageCode:)` to obtain a display name for the language, using [`metadataLanguage`](./metadatalanguage.md)  to create the `Locale`.

## See Also

### Obtaining supported languages
- [let metadataLanguage: Locale.Language?](./metadatalanguage.md)
  The language of the localized properties of this managed app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapp/languages)*