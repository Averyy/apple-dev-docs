# IKRig.ConstraintsCollection.SubSequence

**Framework**: RealityKit  
**Kind**: typealias

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
typealias SubSequence = Slice<IKRig.ConstraintsCollection>
```

#### Discussion

The default subsequence type for collections that don’t define their own is `Slice`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraintscollection/subsequence)*