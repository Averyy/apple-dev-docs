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

For built-in horizontal alignment types, this method returns the mean of all non-`nil` values.

## See Also

- [init(any AlignmentID.Type)](horizontalalignment/init(_:).md)
  Creates a custom horizontal alignment of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/horizontalalignment/combineexplicit(_:))*