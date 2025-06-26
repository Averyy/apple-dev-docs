# controlSize(_:)

**Framework**: FamilyControls  
**Kind**: method

Limits the control size within the view to the given range.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func controlSize<T>(_ range: T) -> some View where T : RangeExpression, T.Bound == ControlSize
```

#### Return Value

A view that constrains the control size of this view within the specified `range`.

#### Discussion

Use this modifier if you’re implementing a custom control or control style that’s  capable of adapting only to a specific range of `ControlSize`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/controlsize(_:)-7jncm)*