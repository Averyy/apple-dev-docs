# target

**Framework**: Translation  
**Kind**: property

The language to translate content into.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
var target: Locale.Language?
```

#### Discussion

If left to its default value of `nil`, the session picks a target language according to the user’s `Locale/preferredLanguages`, and the `source`. Changing this value cancels the previous tasks and creates a new one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/target)*