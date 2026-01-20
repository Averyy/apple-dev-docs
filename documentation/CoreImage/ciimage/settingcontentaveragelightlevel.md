# settingContentAverageLightLevel(_:)

**Framework**: Core Image  
**Kind**: method

Create an image by changing the receiver’s contentAverageLightLevel property.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func settingContentAverageLightLevel(_ average: Float) -> CIImage
```

#### Return Value

 An autoreleased [`CIImage`](ciimage.md).

#### Discussion

Changing this value will alter the behavior of the `CIToneMapHeadroom` and `CISystemToneMap` filters.

- If the value is set to 0.0 or less then the returned image’s [`contentAverageLightLevel`](ciimage/contentaveragelightlevel.md) is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/settingcontentaveragelightlevel(_:))*