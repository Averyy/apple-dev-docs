# maximumImageSize

**Framework**: CarPlay  
**Kind**: property

The expected image size for the image in your @c CPListImageRowItemElement. Images provided will be resized to this size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class var maximumImageSize: CGSize { get }
```

#### Discussion

To properly size your images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement/maximumimagesize)*