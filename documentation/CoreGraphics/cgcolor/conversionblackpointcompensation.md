# conversionBlackPointCompensation

**Framework**: Core Graphics  
**Kind**: property

An option for whether to apply black point compensation when converting between color profiles.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class let conversionBlackPointCompensation: CFString
```

#### Discussion

ICC profiles specify how to convert the lightest level of white between color spaces, but they do not specify how black should be converted. To account for this, set a value of [`true`](https://developer.apple.com/documentation/Swift/true) for this key when creating a color conversion with the [`CGColorConversionInfoCreateFromList`](cgcolorconversioninfocreatefromlist.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/conversionblackpointcompensation)*