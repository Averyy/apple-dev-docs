# rootView

**Framework**: SwiftUI  
**Kind**: property

The root view of the SwiftUI view hierarchy managed by this menu.

**Availability**:
- macOS 14.4+

## Declaration

```swift
var rootView: Content { get set }
```

#### Discussion

Updating this property will immediately update the `items` array, even if the menu is currently visible to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingmenu/rootview)*