# EnumeratedSequence.SubSequence

**Framework**: Swift  
**Kind**: typealias

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

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
typealias SubSequence = Slice<EnumeratedSequence<Base>>
```

#### Discussion

The default subsequence type for collections that don’t define their own is `Slice`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/subsequence)*