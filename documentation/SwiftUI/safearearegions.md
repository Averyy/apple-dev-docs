# SafeAreaRegions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static let all: SafeAreaRegions](./safearearegions/all.md)
  All safe area regions.
- [static let container: SafeAreaRegions](./safearearegions/container.md)
  The safe area defined by the device and containers within the user interface, including elements such as top and bottom bars.
- [static let keyboard: SafeAreaRegions](./safearearegions/keyboard.md)
  The safe area matching the current extent of any software keyboard displayed over the view content.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Staying in the safe areas
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](./view/ignoressafearea%28_,edges%29.md)
  Expands the safe area of a view.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set, alignment: Alignment?) -> some View](./view/ignoressafearea%28_,edges,alignment%29.md)
  Expands the safe area of a view aligning content within the new bounds using the provided alignment.
- [func safeAreaInset(edge:alignment:spacing:content:)](./view/safeareainset%28edge,alignment,spacing,content%29.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(_:)](./view/safeareapadding%28_%29.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](./view/safeareapadding%28_,_%29.md)
  Adds the provided insets into the safe area of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/safearearegions)*