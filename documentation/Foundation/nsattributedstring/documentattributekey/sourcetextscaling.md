# sourceTextScaling

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The text-scaling mode you used when creating the text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let sourceTextScaling: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this property is one of the options of the [`NSTextScalingType`](../../../UIKit/nstextscalingtype.md) type. Some platforms scale fonts to improve their appearance. Include this attribute to specify the original text-scaling mode you used to create the text.

## See Also

### Getting the font-scaling options
- [static let textScaling: NSAttributedString.DocumentAttributeKey](./textscaling.md)
  The text-scaling mode to use when displaying the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/sourcetextscaling)*