# checkForNFC(quickCheck:)

**Framework**: Swift  
**Kind**: method

Do a scan checking for whether the contents are in Normal Form C. When the contents are in NFC, canonical equivalence checks are much faster.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func checkForNFC(quickCheck: Bool) -> Bool
```

#### Discussion

`quickCheck` will check for a subset of NFC contents using the NFCQuickCheck algorithm, which is faster than the full normalization algorithm. However, it cannot detect all NFC contents.

Updates the `isKnownNFC` bit.

> **Note**: O(n)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/checkfornfc(quickcheck:))*