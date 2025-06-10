# maximumGridButtonImageSize

**Framework**: CarPlay  
**Kind**: property

The expected image size for your @c CPGridButton.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
class var maximumGridButtonImageSize: CGSize { get }
```

#### Discussion

To properly size your list images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridtemplate/maximumgridbuttonimagesize)*