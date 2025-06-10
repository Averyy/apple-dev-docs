# CFAttributedStringGetStatisticalWritingDirections(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func CFAttributedStringGetStatisticalWritingDirections(_ attributedString: CFAttributedString!, _ range: CFRange, _ baseDirection: Int8, _ bidiLevels: UnsafeMutablePointer<UInt8>!, _ baseDirections: UnsafeMutablePointer<UInt8>!) -> Bool
```

#### Discussion

If baseDirection is not NSWritingDirectionNatural, result comes from CFAttributedStringGetBidiLevelsAndResolvedDirections; otherwise, it fills bidiLevels by applying a statistical approach (a paragraph is RTL if 40% or more of its words are RTL) to the characters in range. Returns true if the result is not uni-level LTR (in other words, needing further Bidi processing). baseDirection is NSWritingDirection (NSWritingDirectionNatural, NSWritingDirectionLeftToRight, and NSWritingDirectionRightToLeft).  Understands NSWritingDirectionAttributeName values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetstatisticalwritingdirections(_:_:_:_:_:))*