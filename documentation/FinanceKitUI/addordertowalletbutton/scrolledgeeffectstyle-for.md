# scrollEdgeEffectStyle(_:for:)

**Framework**: FinanceKitUI  
**Kind**: method

Configures the scroll edge effect style for scroll views within this hierarchy.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func scrollEdgeEffectStyle(_ style: ScrollEdgeEffectStyle?, for edges: Edge.Set) -> some View
```

#### Discussion

By default, a scroll view will render an automatic edge effect. You use this modifier to change rendered edge effect style.

```None
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectStyle(.hard)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/scrolledgeeffectstyle(_:for:))*