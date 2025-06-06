# combineExplicit(_:)

**Framework**: SwiftUI  
**Kind**: method

Merges a sequence of explicit alignment values produced by this instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func combineExplicit<S>(_ values: S) -> CGFloat? where S : Sequence, S.Element == CGFloat?
```

#### Discussion

For most alignment types, this method returns the mean of all non-`nil` values. However, some types use other rules. For example, [`firstTextBaseline`](verticalalignment/firsttextbaseline.md) returns the minimum value, while [`lastTextBaseline`](verticalalignment/lasttextbaseline.md) returns the maximum value.

## See Also

- [init(any AlignmentID.Type)](verticalalignment/init(_:).md)
  Creates a custom vertical alignment of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/verticalalignment/combineexplicit(_:))*