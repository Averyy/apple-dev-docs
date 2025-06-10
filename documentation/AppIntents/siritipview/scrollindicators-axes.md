# scrollIndicators(_:axes:)

**Framework**: App Intents  
**Kind**: method

Sets the visibility of scroll indicators within this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func scrollIndicators(_ visibility: ScrollIndicatorVisibility, axes: Axis.Set = [.vertical, .horizontal]) -> some View
```

#### Return Value

A view with the specified scroll indicator visibility.

#### Discussion

Use this modifier to hide or show scroll indicators on scrollable content in views like a `ScrollView`, `List`, or `TextEditor`. This modifier applies the prefered visibility to any scrollable content within a view hierarchy.

```swift
ScrollView {
    VStack(alignment: .leading) {
        ForEach(0..<100) {
            Text("Row \($0)")
        }
    }
}
.scrollIndicators(.hidden)
```

Use the `ScrollIndicatorVisibility/hidden` value to indicate that you prefer that views never show scroll indicators along a given axis. Use `ScrollIndicatorVisibility/visible` when you prefer that views show scroll indicators. Depending on platform conventions, visible scroll indicators might only appear while scrolling. Pass `ScrollIndicatorVisibility/automatic` to allow views to decide whether or not to show their indicators.

## Parameters

- `visibility`: The visibility to apply to scrollable views.
- `axes`: The axes of scrollable views that the visibility applies to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/scrollindicators(_:axes:))*