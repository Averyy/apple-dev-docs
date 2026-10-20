# modifier(_:)

**Framework**: DeveloperToolsSupport  
**Kind**: method  
**Role**: Type Method

Attach a `PreviewModifier` to the preview.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
static func modifier(_ modifier: some PreviewModifier) -> PreviewTrait<T>
```

Available when `T` is `Preview.ViewTraits`.

#### Discussion

You can compose modifiers by passing more than one instance of this trait. Composed modifiers will be applied to the preview in order: the first modifier will apply to the body of the preview, the second modifier to the body of the first modifier, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewtrait/modifier(_:))*