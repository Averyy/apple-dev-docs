# layoutPriority(_:)

**Framework**: App Intents  
**Kind**: method

Sets the priority by which a parent layout should apportion space to this child.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func layoutPriority(_ value: Double) -> some View
```

#### Discussion

Views typically have a default priority of `0` which causes space to be apportioned evenly to all sibling views. Raising a view’s layout priority encourages the higher priority view to shrink later when the group is shrunk and stretch sooner when the group is stretched.

```swift
HStack {
    Text("This is a moderately long string.")
        .font(.largeTitle)
        .border(Color.gray)

    Spacer()

    Text("This is a higher priority string.")
        .font(.largeTitle)
        .layoutPriority(1)
        .border(Color.gray)
}
```

In the example above, the first `Text` element has the default priority `0` which causes its view to shrink dramatically due to the higher priority of the second `Text` element, even though all of their other attributes (font, font size and character count) are the same.

A parent layout offers the child views with the highest layout priority all the space offered to the parent minus the minimum space required for all its lower-priority children.

## Parameters

- `value`: The priority by which a parent layout apportions   space to the child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/layoutpriority(_:))*