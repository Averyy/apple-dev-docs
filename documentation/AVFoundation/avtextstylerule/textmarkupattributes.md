# textMarkupAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A dictionary of text style attributes to apply to the text.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var textMarkupAttributes: [String : Any] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,id> * textMarkupAttributes;
```

## Discussion

The supported keys for this dictionary are defined in `CMTextMarkup.h`.

## See Also

### Accessing the style attributes
- [var textSelector: String?](./textselector.md)
  A string that identifies the text the style attributes apply to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/textmarkupattributes)*