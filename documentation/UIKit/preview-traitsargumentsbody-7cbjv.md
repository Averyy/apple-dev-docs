# Preview(_:traits:arguments:body:)

**Framework**: UIKit  
**Kind**: macro

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@freestanding
(declaration) macro Preview<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @PreviewBodyBuilder<UIViewController> body: @escaping @MainActor (T) -> UIViewController)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/preview(_:traits:arguments:body:)-7cbjv)*