# horizontalDisparityAdjustment

**Framework**: Core Video  
**Kind**: property

Indicates a relative shift of the left and right images, which changes the zero parallax plane.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var horizontalDisparityAdjustment: CVAttachmentKeyDefinitionWithDefault<Self.ShouldPropagate, Int32> { get }
```

#### Discussion

The value encoded in normalized image space is measured over the range of -10000 to 10000 mapping to the uniform range [-1.0…1.0]. The interval of 0.0 to 1.0 or 0 to 10000 maps onto the stereo eye view image width. The negative interval 0.0 to -1.0 or 0 to -10000 similarly map onto the stereo eye view image width. The default value of 0 is interpreted if this property is not set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions/horizontaldisparityadjustment)*