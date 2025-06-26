# tintColor

**Framework**: CarPlay  
**Kind**: property

A UIColor used to tint the element. When @c showsImageFullHeight is true, the tint color is applied behind the labels at the bottom of the card. Otherwise, this color is part of the gradient color at the bottom of the card.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@NSCopying
@MainActor var tintColor: UIColor? { get set }
```

#### Discussion

If this value is nil, iOS will use secondarySystemBackground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/tintcolor)*