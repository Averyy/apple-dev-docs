# container

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The margins of the container the view is in.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
static var container: ContentMarginGuide { get }
```

#### Discussion

These margins are the default spacing to use when laying out content in a view. The value depends on the platform, the size of the container, and the position of the view within it.

This guide vends the system layout margins, which range from 16 to 20 points on iPhone and are larger on platforms like tvOS. On iPhone Duo, the margin can also be asymmetric, applying different values on each side of the device when next to a vertical bar. Apply or read the guide instead of writing these values into your layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmarginguide/container)*