# stereoCameraBaseline

**Framework**: Core Media  
**Kind**: property

Indicates the distance between centers of the lenses of the camera system.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@backDeployed(before: macOS 16.0, iOS 19.0, visionOS 3.0)
static var stereoCameraBaseline: CMFormatDescription.Extensions.Key { get }
```

#### Discussion

The value is a CFNumber holding an unsigned 32-bit integer that is interpreted in micrometers or thousandths of a millimeter (e.g., 63123 is 63.123 millimeters). This property is optional and should only be specified if the distance is known.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/key/stereocamerabaseline)*