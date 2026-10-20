# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The system determines the minimize behavior. By default, navigation bars on iOS will minimize when the view has a searchable using the [`toolbarPrincipal`](../searchfieldplacement/toolbarprincipal.md) placement.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var automatic: ToolbarMinimizationBehavior { get }
```

## See Also

### Getting behaviors
- [static let never: ToolbarMinimizationBehavior](./never.md)
  The toolbar cannot be minimized.
- [static let onScrollDown: ToolbarMinimizationBehavior](./onscrolldown.md)
  Minimize when scrolling down.
- [static let onScrollUp: ToolbarMinimizationBehavior](./onscrollup.md)
  Minimize when scrolling up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationbehavior/automatic)*