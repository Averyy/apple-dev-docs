# containerRelativeFrame(_:alignment:_:)

**Framework**: DeviceActivity  
**Kind**: method

Positions this view within an invisible frame with a size relative to the nearest container.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func containerRelativeFrame(_ axes: Axis.Set, alignment: Alignment = .center, _ length: @escaping (CGFloat, Axis) -> CGFloat) -> some View
```

#### Discussion

Use the `View/containerRelativeFrame(_:alignment:)` modifier to specify a size for a view’s width, height, or both that is dependent on the size of the nearest container. Different things can represent a “container” including:

- The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.
- A column of a NavigationSplitView
- A NavigationStack
- A tab of a TabView
- A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones listed above subtracting any safe area insets that might be applied to that container.

The following example will have each purple rectangle occupy the full size of the screen on iOS:

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 0.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .containerRelativeFrame([.horizontal, .vertical])
        }
    }
}
```

Use the `View/containerRelativeFrame(_:count:spacing:alignment:)` modifier to size a view such that multiple views will be visible in the container. When using this modifier, the count refers to the total number of rows or columns that the length of the container size in a particular axis should be divided into. The span refers to the number of rows or columns that the modified view should actually occupy. Thus the size of the element can be described like so:

```swift
let availableWidth = (containerWidth - (spacing * (count - 1)))
let columnWidth = (availableWidth / count)
let itemWidth = (columnWidth * span) + ((span - 1) * spacing)
```

The following example only uses the nearest container size in the horizontal axis, allowing the vertical axis to be determined using the `View/aspectRatio(_:contentMode:)` modifier.

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            Rectangle()
                .fill(.purple)
                .aspectRatio(3.0 / 2.0, contentMode: .fit)
                .containerRelativeFrame(
                    .horizontal, count: 4, span: 3, spacing: 10.0)
        }
    }
}
.safeAreaPadding(.horizontal, 20.0)
```

Use this modifier to apply your own custom logic to adjust the size of the nearest container for your view. The following example will result in the container frame’s width being divided by 3 and using that value as the width of the purple rectangle.

```swift
Rectangle()
    .fill(.purple)
    .aspectRatio(1.0, contentMode: .fill)
    .containerRelativeFrame(
        .horizontal, alignment: .topLeading
    ) { length, axis in
        if axis == .vertical {
            return length / 3.0
        } else {
            return length / 5.0
        }
    }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/containerrelativeframe(_:alignment:_:))*