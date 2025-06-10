# safeAreaBar(edge:alignment:spacing:content:)

**Framework**: FinanceKitUI  
**Kind**: method

Renders the provided content appropriate to be displayed as a custom bar.

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
func safeAreaBar(edge: VerticalEdge, alignment: HorizontalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> some View) -> some View
```

#### Discussion

Similar to a `View/safeAreaInset(edge:alignment:spacing:content)` modifier, the modified view will have its vertical safe area inset by the height of the content.

In addition to adjusting the safe area, the bar modifier configures the `content` to support views to automatically extend the edge effect of any scroll view’s the bar adjusts safe area of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/safeareabar(edge:alignment:spacing:content:)-3hzkt)*