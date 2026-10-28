# dynamicTypeSize(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Limits the Dynamic Type size within the view to the given range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func dynamicTypeSize<T>(_ range: T) -> some View where T : RangeExpression, T.Bound == DynamicTypeSize
```

**Other overloads**:

```swift
nonisolated
func dynamicTypeSize(_ size: DynamicTypeSize) -> some View
```

## Return Value

A view that constrains the Dynamic Type size of this view within the specified `range`.

## Discussion

As an example, you can constrain the maximum Dynamic Type size in `ContentView` to be no larger than [`DynamicTypeSize.large`](../dynamictypesize/large.md):

```swift
ContentView()
    .dynamicTypeSize(...DynamicTypeSize.large)
```

If the Dynamic Type size is limited to multiple ranges, the result is their intersection:

```swift
ContentView() // Dynamic Type sizes are from .small to .large
    .dynamicTypeSize(.small...)
    .dynamicTypeSize(...DynamicTypeSize.large)
```

A specific Dynamic Type size can still be set after a range is applied:

```swift
ContentView() // Dynamic Type size is .xLarge
    .dynamicTypeSize(.xLarge)
    .dynamicTypeSize(...DynamicTypeSize.large)
```

When limiting the Dynamic Type size, consider if adding a large content view with [`accessibilityShowsLargeContentViewer()`](./accessibilityshowslargecontentviewer%28%29.md) would be appropriate.

## Parameters

- `range`: The range of sizes that are allowed in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dynamictypesize(_:)-26aj0)*