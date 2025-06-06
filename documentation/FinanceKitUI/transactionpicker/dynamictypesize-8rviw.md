# dynamicTypeSize(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Limits the Dynamic Type size within the view to the given range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func dynamicTypeSize<T>(_ range: T) -> some View where T : RangeExpression, T.Bound == DynamicTypeSize
```

#### Return Value

A view that constrains the Dynamic Type size of this view within the specified `range`.

#### Discussion

As an example, you can constrain the maximum Dynamic Type size in `ContentView` to be no larger than `DynamicTypeSize/large`:

```None
ContentView()
    .dynamicTypeSize(...DynamicTypeSize.large)
```

If the Dynamic Type size is limited to multiple ranges, the result is their intersection:

```None
ContentView() // Dynamic Type sizes are from .small to .large
    .dynamicTypeSize(.small...)
    .dynamicTypeSize(...DynamicTypeSize.large)
```

A specific Dynamic Type size can still be set after a range is applied:

```None
ContentView() // Dynamic Type size is .xLarge
    .dynamicTypeSize(.xLarge)
    .dynamicTypeSize(...DynamicTypeSize.large)
```

When limiting the Dynamic Type size, consider if adding a large content view with `View/accessibilityShowsLargeContentViewer()` would be appropriate.

## Parameters

- `range`: The range of sizes that are allowed in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/dynamictypesize(_:)-8rviw)*