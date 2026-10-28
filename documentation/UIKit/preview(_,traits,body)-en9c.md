# Preview(_:traits:body:)

**Framework**: UIKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@freestanding(declaration)
macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., @PreviewMacroBodyBuilder<UIViewController> body: @escaping @MainActor () -> UIViewController)
```

## See Also

### Macros
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> UIView)](./preview%28_,traits,body%29-c7kr.md)
- [macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIView)](./preview%28_,traits,arguments,body%29-6gm4c.md)
- [macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> UIViewController)](./preview%28_,traits,arguments,body%29-7cbjv.md)
- [var UIKIT_HAS_UIFOUNDATION_SYMBOLS: Int32](./uikit_has_uifoundation_symbols.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/preview(_:traits:body:)-en9c)*