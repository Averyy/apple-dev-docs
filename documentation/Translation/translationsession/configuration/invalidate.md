# invalidate()

**Framework**: Translation  
**Kind**: method

Invalidate the current translation session to re-run it again with new content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
mutating func invalidate()
```

#### Discussion

Call this method when you want to translate new content using the same source and target languages. When you do, it causes the `View/translationTask(_:action:)` function to call its `action` closure and translate the content again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration/invalidate())*