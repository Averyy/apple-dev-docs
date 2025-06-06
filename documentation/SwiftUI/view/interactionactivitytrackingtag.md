# interactionActivityTrackingTag(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets a tag that you use for tracking interactivity.

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
nonisolated
func interactionActivityTrackingTag(_ tag: String) -> some View
```

#### Return Value

A view that uses a tracking tag.

#### Discussion

The following example tracks the scrolling activity of a [`List`](list.md):

```swift
List {
    Section("Today") {
        ForEach(messageStore.today) { message in
            Text(message.title)
        }
    }
}
.interactionActivityTrackingTag("MessagesList")
```

The resolved activity tracking tag is additive, so using the modifier across the view hierarchy builds the tag from top to bottom. The example below shows a hierarchical usage of this modifier with the resulting tag `Home-Feed`:

```swift
var body: some View {
    Home()
        .interactionActivityTrackingTag("Home")
}

struct Home: View {
    var body: some View {
        List {
            Text("A List Item")
            Text("A Second List Item")
            Text("A Third List Item")
        }
        .interactionActivityTrackingTag("Feed")
    }
}
```

## Parameters

- `tag`: The tag used to track user interactions   hosted by this view as activities.

## See Also

- [func disabled(Bool) -> some View](view/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [var isEnabled: Bool](environmentvalues/isenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [func invalidatableContent(Bool) -> some View](view/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/interactionactivitytrackingtag(_:))*