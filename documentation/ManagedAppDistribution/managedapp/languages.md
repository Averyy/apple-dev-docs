# languages

**Framework**: ManagedAppDistribution  
**Kind**: property

The app’s supported languages.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
let languages: [Locale.Language]
```

#### Discussion

> 💡 **Tip**: Use `Locale.localizedString(forLanguageCode:)` to obtain a display name for the language, using [`metadataLanguage`](managedapp/metadatalanguage.md)  to create the `Locale`.

Use `Locale.localizedString(forLanguageCode:)` to obtain a display name for the language, using [`metadataLanguage`](managedapp/metadatalanguage.md)  to create the `Locale`.

## See Also

- [let metadataLanguage: Locale.Language?](managedapp/metadatalanguage.md)
  The language of the localized properties of this managed app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapp/languages)*