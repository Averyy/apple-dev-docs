# layoutProperties

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

Properties of a layout container.

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

## Discussion

Implement this property in a type that conforms to the [`Layout`](../layout.md) protocol to characterize your custom layout container. For example, you can indicate that your layout has a vertical [`stackOrientation`](../layoutproperties/stackorientation.md):

```swift
extension BasicVStack {
    static var layoutProperties: LayoutProperties {
        var properties = LayoutProperties()
        properties.stackOrientation = .vertical
        return properties
    }
}
```

If you don’t implement this property in your custom layout, the protocol provides a default implementation, namely [`layoutProperties`](./layoutproperties-6h7w0.md), that returns a [`LayoutProperties`](../layoutproperties.md) instance with default values.

## Default Implementations

### Layout Implementations
- [static var layoutProperties: LayoutProperties](./layoutproperties-6h7w0.md)
  The default property values for a layout.

## See Also

### Reporting layout container characteristics
- [func explicitAlignment(of:in:proposal:subviews:cache:)](./explicitalignment%28of,in,proposal,subviews,cache%29.md)
  Returns the position of the specified horizontal alignment guide along the x axis.
- [func spacing(subviews: Self.Subviews, cache: inout Self.Cache) -> ViewSpacing](./spacing%28subviews,cache%29.md)
  Returns the preferred spacing values of the composite view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/layoutproperties)*