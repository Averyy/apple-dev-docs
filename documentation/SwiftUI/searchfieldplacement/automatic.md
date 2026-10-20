# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

SwiftUI places the search field automatically.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let automatic: SearchFieldPlacement
```

#### Discussion

Placement of the search field depends on the platform:

- In iOS, iPadOS, and macOS, the search field appears in the toolbar.
- In tvOS and watchOS, the search field appears inline with its content.

## See Also

### Getting a search field placement
- [static let navigationBarDrawer: SearchFieldPlacement](./navigationbardrawer.md)
  The search field appears in the navigation bar.
- [static func navigationBarDrawer(displayMode: SearchFieldPlacement.NavigationBarDrawerDisplayMode) -> SearchFieldPlacement](./navigationbardrawer%28displaymode%29.md)
  The search field appears in the navigation bar using the specified display mode.
- [static var sidebar: SearchFieldPlacement](./sidebar.md)
  The search field appears in the sidebar of a navigation view.
- [static let toolbar: SearchFieldPlacement](./toolbar.md)
  The search field appears in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchfieldplacement/automatic)*