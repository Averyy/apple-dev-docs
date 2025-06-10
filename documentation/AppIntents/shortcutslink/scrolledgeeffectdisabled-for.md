# scrollEdgeEffectDisabled(_:for:)

**Framework**: App Intents  
**Kind**: method

Disables any scroll edge effects for scroll views within this hierarchy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func scrollEdgeEffectDisabled(_ disabled: Bool = true, for edges: Edge.Set = .all) -> some View
```

#### Discussion

By default, a scroll view will render an automatic edge effect style. You use this modifier to disable the rendering of any edge effects for scroll views within this hierarchy.

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectDisabled()
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/scrolledgeeffectdisabled(_:for:))*