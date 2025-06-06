# SafeAreaRegions

**Framework**: SwiftUI  
**Kind**: struct

A set of symbolic safe area regions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct SafeAreaRegions
```

## Topics

### Getting safe area regions
- [static let all: SafeAreaRegions](safearearegions/all.md)
  All safe area regions.
- [static let container: SafeAreaRegions](safearearegions/container.md)
  The safe area defined by the device and containers within the user interface, including elements such as top and bottom bars.
- [static let keyboard: SafeAreaRegions](safearearegions/keyboard.md)
  The safe area matching the current extent of any software keyboard displayed over the view content.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](view/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func safeAreaInset(edge:alignment:spacing:content:)](view/safeareainset(edge:alignment:spacing:content:).md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(_:)](view/safeareapadding(_:).md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](view/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/safearearegions)*