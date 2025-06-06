# isIdeographic

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the scalar is considered to be a CJKV (Chinese, Japanese, Korean, and Vietnamese) or other siniform (Chinese writing-related) ideograph.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isIdeographic: Bool { get }
```

#### Discussion

This property roughly defines the class of “Chinese characters” and does not include characters of other logographic scripts such as Cuneiform or Egyptian Hieroglyphs.

This property corresponds to the “Ideographic” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isideographic)*