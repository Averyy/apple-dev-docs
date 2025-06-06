# union(_:edges:)

**Framework**: SwiftUI  
**Kind**: method

Gets a new value that merges the spacing preferences of another spacing instance with this instance for a specified set of edges.

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
func union(_ other: ViewSpacing, edges: Edge.Set = .all) -> ViewSpacing
```

#### Return Value

A new view spacing preferences instance with the merged values.

#### Discussion

This method behaves like [`formUnion(_:edges:)`](viewspacing/formunion(_:edges:).md), except that it creates a copy of the original spacing preferences instance before merging, leaving the original instance unmodified.

## Parameters

- `other`: Another spacing preferences instance to merge with this one.
- `edges`: The edges to merge. Edges that you don’t specify are   unchanged after the method completes.

## See Also

- [func formUnion(ViewSpacing, edges: Edge.Set)](viewspacing/formunion(_:edges:).md)
  Merges the spacing preferences of another spacing instance with this instance for a specified set of edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewspacing/union(_:edges:))*