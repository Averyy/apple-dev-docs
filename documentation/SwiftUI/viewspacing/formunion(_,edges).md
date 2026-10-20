# formUnion(_:edges:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Merges the spacing preferences of another spacing instance with this instance for a specified set of edges.

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
mutating func formUnion(_ other: ViewSpacing, edges: Edge.Set = .all)
```

#### Discussion

When you merge another spacing preference instance with this one, this instance ends up with the greater of its original value or the other instance’s value for each of the specified edges. You can call the method repeatedly with each value in a collection to merge a collection of preferences. The result has the smallest preferences on each edge that meets the largest requirements of all the inputs for that edge.

If you want to merge preferences without modifying the original instance, use [`union(_:edges:)`](./union%28_,edges%29.md) instead.

## Parameters

- `other`: Another spacing preferences instances to merge with this one.
- `edges`: The edges to merge. Edges that you don’t specify are unchanged after the method completes.

## See Also

### Merging spacing instances
- [func union(ViewSpacing, edges: Edge.Set) -> ViewSpacing](./union%28_,edges%29.md)
  Gets a new value that merges the spacing preferences of another spacing instance with this instance for a specified set of edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewspacing/formunion(_:edges:))*