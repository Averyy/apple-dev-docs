# isUnifiedIdeograph

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the scalar is one of the unified CJK ideographs in the Unicode Standard.

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
var isUnifiedIdeograph: Bool { get }
```

#### Discussion

This property is false for CJK punctuation and symbols, as well as for compatibility ideographs (which canonically decompose to unified ideographs).

This property corresponds to the “Unified_Ideograph” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isunifiedideograph)*