# accessibilityDefaultFocus(_:_:)

**Framework**: Assignables  
**Kind**: method

Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func accessibilityDefaultFocus<Value>(_ binding: AccessibilityFocusState<Value>.Binding, _ value: Value) -> some View where Value : Hashable
```

#### Discussion

Accessibility default focus is evaluated when a scene appears and an accessibility technology like VoiceOver focuses on its content, when an accessibility focus state binding update moves focus automatically, and when the layout of a scene changes and the accessibility technology must refocus on new content.

In the following example, an accessibility technology, like VoiceOver, automatically lands on the title of the playlist as the most important view to initially have focus on, rather than navigating through all controls to understand what the primary content of the view is.

```None
var body: some View {
    VStack {
        PlayerControls(currentSong: $currentSong)
        Text(playlist.title)
            .font(.title)
            .accessibilityFocused($focusedField, equals: .title)
        PlaylistEntries(entries: playlist.entries)
    }
    .accessibilityDefaultFocus($focusedField, .title)
}
```

## Parameters

- `binding`: An accessibility focus state binding to update when   evaluating default accessibility focus.
- `value`: The value to set the binding to during evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/accessibilitydefaultfocus(_:_:))*