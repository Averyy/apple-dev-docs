# scrollTargetLayout(isEnabled:)

**Framework**: App Intents  
**Kind**: method

Configures the outermost layout as a scroll target layout.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func scrollTargetLayout(isEnabled: Bool = true) -> some View
```

#### Discussion

This modifier works together with the `ViewAlignedScrollTargetBehavior` to ensure that scroll views align to view based content.

Apply this modifier to layout containers like `LazyHStack` or `VStack` within a `ScrollView` that contain the main repeating content of your `ScrollView`.

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 10.0) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollTargetBehavior(.viewAligned)
```

Scroll target layouts act as a convenience for applying a `View/scrollTarget(isEnabled:)` modifier to each views in the layout.

A scroll target layout will ensure that any target layout nested within the primary one will not also become a scroll target layout.

```swift
LazyHStack { // a scroll target layout
    VStack { ... } // not a scroll target layout
    LazyHStack { ... } // also not a scroll target layout
}
.scrollTargetLayout()
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/scrolltargetlayout(isenabled:))*