# editor

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The editor role.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var editor: ToolbarRole { get }
```

#### Discussion

Use this role for a toolbar that primarily displays controls geared towards editing document-like content. In iPadOS, this will leading align the navigation title, allow for toolbar items to occupy the center of the navigation bar, and provide a custom appearance for any back button present in the toolbar.

## See Also

### Behavior-specific roles
- [static var browser: ToolbarRole](./browser.md)
  The browser role.
- [static var navigationStack: ToolbarRole](./navigationstack.md)
  The navigationStack role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarrole/editor)*