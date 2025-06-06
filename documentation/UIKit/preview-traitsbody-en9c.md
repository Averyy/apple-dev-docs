# Preview(_:traits:body:)

**Framework**: UIKit  
**Kind**: macro

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@freestanding
(declaration) macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., @PreviewMacroBodyBuilder<UIViewController> body: @escaping @MainActor () -> UIViewController)
```

## See Also

- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIView)](preview(_:traits:body:)-c7kr.md)
- [var UIKIT_HAS_UIFOUNDATION_SYMBOLS: Int32](uikit_has_uifoundation_symbols.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/preview(_:traits:body:)-en9c)*