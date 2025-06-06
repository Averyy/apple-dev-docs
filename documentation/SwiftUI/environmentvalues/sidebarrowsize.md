# sidebarRowSize

**Framework**: SwiftUI  
**Kind**: property

The current size of sidebar rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var sidebarRowSize: SidebarRowSize { get set }
```

#### Discussion

On macOS, reflects the value of the “Sidebar icon size” in System Settings’ Appearance settings.

This can be used to update the content shown in the sidebar in response to this size. And it can be overridden to force a sidebar to a particularly size, regardless of the user preference.

On other platforms, the value is always `.medium` and setting a different value has no effect.

SwiftUI views like `Label` automatically adapt to the sidebar row size.

## See Also

- [enum SidebarRowSize](sidebarrowsize.md)
  The standard sizes of sidebar rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/sidebarrowsize)*