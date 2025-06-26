# navigationLinkIndicatorVisibility(_:)

**Framework**: MusicKit  
**Kind**: method

Configures whether navigation links show a disclosure indicator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func navigationLinkIndicatorVisibility(_ visibility: Visibility) -> some View
```

#### Discussion

If you need to detect whether the navigation disclosure indicator should be shown for the current view, read the `EnvironmentValues/navigationLinkIndicatorVisibility` environment value.

The following example hides the indicator for all links in the list. The indicator can be hidden for a specific link by placing the modifier on the `NavigationLink` itself.

```swift
struct NoIndicatorLink: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("See detail") {
                    Text("Detail view")
                }
            }
            .navigationLinkIndicatorVisibility(.hidden)
        }
    }
}
```

> ❗ **Important**: Setting the link indicator visibility to `.visible` is only supported for navigation links contained in a `List` built with the Xcode 16 SDKs and earlier. Current releases support setting the indicator visibility to `.visible` regardless of whether the link is within a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/navigationlinkindicatorvisibility(_:))*