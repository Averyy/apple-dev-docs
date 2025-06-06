# textScaling

**Framework**: Foundation  
**Kind**: property

The text-scaling mode to use when displaying the text.

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
static let textScaling: NSAttributedString.DocumentAttributeKey
```

#### Discussion

The value of this property is one of the options of the [`NSTextScalingType`](https://developer.apple.com/documentation/UIKit/NSTextScalingType) type. Some platforms scale fonts to improve their appearance. When saving a document, include this attribute to specify the type of scaling to apply to the text at display time.

## See Also

- [static let sourceTextScaling: NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey/sourcetextscaling.md)
  The text-scaling mode you used when creating the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/textscaling)*