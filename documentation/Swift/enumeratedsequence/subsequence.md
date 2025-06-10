# EnumeratedSequence.SubSequence

**Framework**: Swift  
**Kind**: typealias

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

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
typealias SubSequence = Slice<EnumeratedSequence<Base>>
```

#### Discussion

The default subsequence type for collections that don’t define their own is `Slice`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/subsequence)*