# target

**Framework**: Translation  
**Kind**: property

The language to translate content into.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
var target: Locale.Language?
```

#### Discussion

If left to its default value of `nil`, the session picks a target language according to the `source` and the person’s [`preferredLanguages`](https://developer.apple.com/documentation/foundation/locale/preferredlanguages). Changing this value cancels the previous tasks and creates a new one.

## See Also

- [var source: Locale.Language?](translationsession/configuration/source.md)
  The language to translate content from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/target)*