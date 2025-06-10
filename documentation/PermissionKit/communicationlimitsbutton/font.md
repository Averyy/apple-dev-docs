# font(_:)

**Framework**: PermissionKit  
**Kind**: method

Sets the default font for text in this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 26.0+ (Beta)
- watchOS 6.0+

## Declaration

```swift
nonisolated
func font(_ font: Font?) -> some View
```

#### Return Value

A view with the default font set to the value you supply.

#### Discussion

Use `font(_:)` to apply a specific font to all of the text in a view.

The example below shows the effects of applying fonts to individual views and to view hierarchies. Font information flows down the view hierarchy as part of the environment, and remains in effect unless overridden at the level of an individual view or view container.

Here, the outermost `VStack` applies a 16-point system font as a default font to views contained in that `VStack`. Inside that stack, the example applies a `Font/largeTitle` font to just the first text view; this explicitly overrides the default. The remaining stack and the views contained with it continue to use the 16-point system font set by their containing view:

```None
VStack {
    Text("Font applied to a text view.")
        .font(.largeTitle)

    VStack {
        Text("These 2 text views have the same font")
        Text("applied to their parent hierarchy")
    }
}
.font(.system(size: 16, weight: .light, design: .default))
```

## Parameters

- `font`: The default font to use in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/font(_:))*