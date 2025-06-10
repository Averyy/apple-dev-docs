# horizontalDisparityAdjustment

**Framework**: Core Media  
**Kind**: property

Indicates a relative shift of the left and right images, which changes the zero parallax plane.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@backDeployed(before: macOS 16.0, iOS 19.0, visionOS 3.0)
static var horizontalDisparityAdjustment: CMFormatDescription.Extensions.Key { get }
```

#### Discussion

The value encoded in normalized image space is  a signed 32-bit integer measured over the range of -10000 to 10000 mapping to the uniform range [-1.0…1.0]. The interval of 0.0 to 1.0 or 0 to 10000 maps onto the stereo eye view image width. The negative interval 0.0 to -1.0 or 0 to -10000 similarly maps onto the stereo eye view image width.

The default value of 0 is interpreted if this property is not set. If the property is not set, NULL may be set and retrieved. The NULL value should be interpreted as meaning 0.

This property is optional and should only be specified if a disparity adjustment including 0 is known.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/key/horizontaldisparityadjustment)*