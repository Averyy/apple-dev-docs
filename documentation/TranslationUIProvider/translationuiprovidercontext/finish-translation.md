# finish(translation:)

**Framework**: TranslationUIProvider  
**Kind**: method  
**Required**: Yes

Completes the translation after which the framework closes the sheet.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
func finish(translation: AttributedString?)
```

## Parameters

- `translation`: The optional translation result. If   and the source text allows replacement, no replacement takes place. If non-  and the source text doesn’t allow replacement, framework ignores the parameter. It is recommended that providers attempt to preserve any attributes of the source text, but it is not a requirement.

## See Also

- [func expandSheet()](translationuiprovidercontext/expandsheet.md)
  The framework requests that the sheet expand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translationuiprovider/translationuiprovidercontext/finish(translation:))*