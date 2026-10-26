# layoutProperties

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default property values for a layout.

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
static var layoutProperties: LayoutProperties { get }
```

#### Discussion

If you don’t implement the [`layoutProperties`](./layoutproperties.md) method in your custom layout, the protocol uses this default implementation instead, which returns a [`LayoutProperties`](../layoutproperties.md) instance with default values. The properties instance contains information about the layout container, like a [`stackOrientation`](../layoutproperties/stackorientation.md) property that indicates the container’s major axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/layoutproperties-6h7w0)*