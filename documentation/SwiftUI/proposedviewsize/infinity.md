# infinity

**Framework**: SwiftUI  
**Kind**: property

A size proposal that contains infinity in both dimensions.

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
static let infinity: ProposedViewSize
```

#### Discussion

Both dimensions contain doc://com.apple.documentation/documentation/CoreFoundation/CGFloat/1454161-infinity in this size proposal. Subviews of a custom layout return their maximum size when you propose this value using the [`dimensions(in:)`](layoutsubview/dimensions(in:).md) method. A custom layout should also return its maximum size from the [`sizeThatFits(proposal:subviews:cache:)`](layout/sizethatfits(proposal:subviews:cache:).md) method for this value.

## See Also

- [static let zero: ProposedViewSize](proposedviewsize/zero.md)
  A size proposal that contains zero in both dimensions.
- [static let unspecified: ProposedViewSize](proposedviewsize/unspecified.md)
  The proposed size with both dimensions left unspecified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/proposedviewsize/infinity)*