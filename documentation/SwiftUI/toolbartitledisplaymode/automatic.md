# automatic

**Framework**: SwiftUI  
**Kind**: property

The automatic mode.

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
static var automatic: ToolbarTitleDisplayMode { get }
```

#### Discussion

For root content in a navigation stack in iOS, iPadOS, or tvOS this behavior will:

- Default to [`large`](toolbartitledisplaymode/large.md) when a navigation title is configured.
- Default to [`inline`](toolbartitledisplaymode/inline.md) when no navigation title is provided.

In all platforms, content pushed onto a navigation stack will use the behavior of the content already on the navigation stack. This has no effect in macOS.

## See Also

- [static var inline: ToolbarTitleDisplayMode](toolbartitledisplaymode/inline.md)
  The inline mode.
- [static var inlineLarge: ToolbarTitleDisplayMode](toolbartitledisplaymode/inlinelarge.md)
  The inline large mode.
- [static var large: ToolbarTitleDisplayMode](toolbartitledisplaymode/large.md)
  The large mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbartitledisplaymode/automatic)*