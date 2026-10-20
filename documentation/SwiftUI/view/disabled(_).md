# disabled(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a condition that controls whether someone can interact with this view.

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
func disabled(_ disabled: Bool) -> some View
```

#### Return Value

A view that controls whether someone can interact with this view.

#### Discussion

Add this modifier to a view to indicate whether it responds to interactions such as a tap, click, or gesture. The following example disables a [`Button`](../button.md) when the Boolean value `isLoading` is `true`:

```swift
@State private var isLoading: Bool = false

var body: some View {
    Button("Load") { }
        .disabled(isLoading)
}
```

Add this modifier to a container, such as a [`VStack`](../vstack.md), to indicate whether views in the container are currently interactive, and to override any `.disabled(_:)` modifiers you set on views within the container or view hierarchy. In the following example, the `.disabled(true)` modifier on the [`VStack`](../vstack.md) disables all of the [`Button`](../button.md) instances in the stack, even the button that has the modifier `.disabled(false)`.

```swift
VStack {
    Button("One") {}
        .disabled(false)
    Button("Two") {}
    Button("Three") {}
}
.disabled(true)
```

## Parameters

- `disabled`: A Boolean value that determines whether someone can interact with this view.

## See Also

### Managing view interaction
- [var isEnabled: Bool](../environmentvalues/isenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [func interactionActivityTrackingTag(String) -> some View](./interactionactivitytrackingtag%28_%29.md)
  Sets a tag that you use for tracking interactivity.
- [func invalidatableContent(Bool) -> some View](./invalidatablecontent%28_%29.md)
  Mark the receiver as their content might be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/disabled(_:))*