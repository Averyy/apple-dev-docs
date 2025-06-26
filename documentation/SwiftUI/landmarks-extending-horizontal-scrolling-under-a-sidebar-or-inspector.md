# Landmarks: Extending horizontal scrolling under a sidebar or inspector

**Framework**: SwiftUI

Improve your horizontal scrollbar’s appearance by extending it under a sidebar or inspector.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

The Landmarks app lets people explore interesting sites around the world. Whether it’s a national park near their home or a far-flung location on a different continent, the app provides a way for people to organize and mark their adventures and receive custom activity badges along the way.

This sample demonstrates how to extend horizontal scrolling under a sidebar or inspector. Within each continent section in `LandmarksView`, an instance of `LandmarkHorizontalListView` shows a horizontally scrolling list of landmark views. When open, the landmark views can scroll underneath the sidebar or inspector.

![An image of the landmarks view on an iPad, with the sidebar visible and some landmarks visible under the sidebar.](https://docs-assets.developer.apple.com/published/a4b11a4a06f283b210c25071788c472e/Landmarks-Building-an-app-with-Liquid-Glass-3%402x.png)

#### Configure the Scroll View

To achieve this effect, the sample configures the `LandmarkHorizontalListView` so it touches the leading and trailing edges. When a scroll view touches the sidebar or inspector, the system automatically adjusts it to scroll under the sidebar or inspector and then off the edge of the screen.

The sample adds a [`Spacer`](spacer.md) at the beginning of the [`ScrollView`](scrollview.md) to inset the content so it aligns with the title padding:

```swift
ScrollView(.horizontal, showsIndicators: false) {
    LazyHStack(spacing: Constants.standardPadding) {
        Spacer()
            .frame(width: Constants.standardPadding)
        ForEach(landmarkList) { landmark in
            //...
        }
    }
}
```

## See Also

- [Landmarks: Applying a background extension effect](landmarks-applying-a-background-extension-effect.md)
  Configure an image to blur and extend under a sidebar or inspector panel.
- [Landmarks: Refining the system provided Liquid Glass effect in toolbars](landmarks-refining-the-system-provided-glass-effect-in-toolbars.md)
  Organize toolbars into related groupings to improve their appearance and utility.
- [Landmarks: Displaying custom activity badges](landmarks-displaying-custom-activity-badges.md)
  Provide people with a way to mark their adventures by displaying animated custom activity badges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/landmarks-extending-horizontal-scrolling-under-a-sidebar-or-inspector)*