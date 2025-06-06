# widgetAccentedRenderingMode(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the how to render an `Image` when using the `WidgetKit/WidgetRenderingMode/accented` mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func widgetAccentedRenderingMode(_ renderingMode: WidgetAccentedRenderingMode?) -> some View
```

#### Discussion

```swift
var body: some View {
    VStack {
        Image("cat_full")
            .resizable()
            .widgetAccentedRenderingMode(.fullColor)
    }
}
```

> ❗ **Important**: If the `Image` is a subview for a group that has `widgetAccentable(true)` applied, this modifier may conflict.

If the `Image` is a subview for a group that has `widgetAccentable(true)` applied, this modifier may conflict.

## Parameters

- `renderingMode`: A constant describing how the    should be rendered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/widgetaccentedrenderingmode(_:))*