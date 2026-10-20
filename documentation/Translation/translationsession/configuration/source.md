# source

**Framework**: Translation  
**Kind**: property  
**Role**: Instance Property

The language to translate content from.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
var source: Locale.Language?
```

#### Discussion

If left to its default value of `nil`, the session tries to identify the source language automatically, and prompts the person to choose a source language if it’s unclear. Changing this value cancels the previous task and creates a new one.

## See Also

### Specifying translation languages
- [var target: Locale.Language?](./target.md)
  The language to translate content into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/source)*