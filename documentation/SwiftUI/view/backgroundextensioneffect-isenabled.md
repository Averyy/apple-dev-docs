# backgroundExtensionEffect(isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func backgroundExtensionEffect(isEnabled: Bool) -> some View
```

#### Discussion

Use this modifier when you want to create copies outside of the safe area so the view and its copies together can function as backgrounds for other elements on top. The most common use case is to apply this to a view in the detail column of a navigation split view so it can extend under the sidebar or inspector region to provide seamless immersive visuals.

```swift
@State private var extendBackground: Bool = true

NavigationSplitView {
    // sidebar content
} detail: {
    ZStack {
        BannerView()
            .backgroundExtensionEffect(isEnabled: extendBackground)
    }
}
.inspector(isPresented: $showInspector) {
    // inspector content
}
```

Apply this modifier with discretion. This should often be used with only a single instance of background content with consideration of visual clarity and performance.

> **Note**: This modifier will clip the view to prevent copies from overlapping with each other.

## Parameters

- `isEnabled`: Should the extension effect be active or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect(isenabled:))*