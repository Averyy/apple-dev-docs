# ToolbarVerticalCompressionBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A behavior that determines how bars compress when the system places different types of bars together and space is constrained.

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
struct ToolbarVerticalCompressionBehavior
```

## Overview

Use this with the [`toolbarVerticalCompressionBehavior(_:)`](./view/toolbarverticalcompressionbehavior%28_%29.md) modifier to control which items compress first when space is limited.

## Topics

### Getting compression behavior options
- [static let automatic: ToolbarVerticalCompressionBehavior](./toolbarverticalcompressionbehavior/automatic.md)
  The automatic compression behavior.
- [static let prefersTabBar: ToolbarVerticalCompressionBehavior](./toolbarverticalcompressionbehavior/preferstabbar.md)
  A compression behavior that prefers keeping the tab bar visible.
- [static let prefersToolbarItems: ToolbarVerticalCompressionBehavior](./toolbarverticalcompressionbehavior/preferstoolbaritems.md)
  A compression behavior that prefers keeping toolbar items visible.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring vertical toolbar behavior
- [func toolbarVerticalBehavior(ToolbarVerticalBehavior) -> some View](./view/toolbarverticalbehavior%28_%29.md)
  Sets the behavior for the vertical bar.
- [struct ToolbarVerticalBehavior](./toolbarverticalbehavior.md)
  A behavior that determines whether the vertical bar is used.
- [func toolbarVerticalCompressionBehavior(ToolbarVerticalCompressionBehavior) -> some View](./view/toolbarverticalcompressionbehavior%28_%29.md)
  Sets how bars should compress when different types of toolbars are hosted together and space is constrained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarverticalcompressionbehavior)*