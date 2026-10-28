# controlSize(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Limits the control size within the view to the given range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func controlSize<T>(_ range: T) -> some View where T : RangeExpression, T.Bound == ControlSize
```

**Other overloads**:

```swift
nonisolated
func controlSize(_ controlSize: ControlSize) -> some View
```

## Return Value

A view that constrains the control size of this view within the specified `range`.

## Discussion

Use this modifier if you’re implementing a custom control or control style that’s  capable of adapting only to a specific range of [`ControlSize`](../controlsize.md).

For example, your implementation of a custom control could constrain the maximum `EnvironmentValue/controlSize` in its `ContentView`’s environment to `.regular` like this:

```swift
struct CustomControl: View {
    var body: some View {
        ContentView()
            .controlSize(... .regular)
    }

    private struct ContentView() {
        @Environment(\.controlSize) private var controlSize

        var body: some View {
            // controlSize won't exceed .regular
        }
    }
}
```

If the control size is limited to multiple ranges, the result is their intersection:

```swift
ContentView() // Control sizes are from .small to .large
    .controlSize(.small...)
    .controlSize(... .large)
```

A specific control size can still be set after a range is applied:

```swift
HStack {
    Button("Create", action: ...) // Control size will be .mini
        .controlSize(.mini)
}
.controlSize(.small ... .large)
```

## Parameters

- `range`: The range of sizes that are allowed in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/controlsize(_:)-rvbn)*