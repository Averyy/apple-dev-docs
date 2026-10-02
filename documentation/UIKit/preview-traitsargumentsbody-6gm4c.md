# Preview(_:traits:arguments:body:)

**Framework**: UIKit  
**Kind**: macro

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@freestanding
(declaration) macro Preview<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @PreviewBodyBuilder<UIView> body: @escaping @MainActor (T) -> UIView)
```

## See Also

- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIView)](preview(_:traits:body:)-c7kr.md)
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIViewController)](preview(_:traits:body:)-en9c.md)
- [macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIViewController)](preview(_:traits:arguments:body:)-7cbjv.md)
- [var UIKIT_HAS_UIFOUNDATION_SYMBOLS: Int32](uikit_has_uifoundation_symbols.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/preview(_:traits:arguments:body:)-6gm4c)*