# linguisticTags(in:scheme:options:orthography:tokenRanges:)

**Framework**: Swift  
**Kind**: method

Returns an array of linguistic tags for the specified range and requested tags within the receiving string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func linguisticTags<T, R>(in range: R, scheme tagScheme: T, options opts: NSLinguisticTagger.Options = [], orthography: NSOrthography? = nil, tokenRanges: UnsafeMutablePointer<[Range<Self.Index>]>? = nil) -> [String] where T : StringProtocol, R : RangeExpression, R.Bound == String.Index
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/linguistictags(in:scheme:options:orthography:tokenranges:))*