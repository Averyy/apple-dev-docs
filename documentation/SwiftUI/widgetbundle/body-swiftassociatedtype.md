# Body

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type of widget that represents the content of the bundle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
associatedtype Body : Widget
```

#### Discussion

When you support more than one widget, Swift infers this type from your implementation of the required [`body`](widgetbundle/body-swift.property.md) property.

## See Also

- [var body: Self.Body](widgetbundle/body-swift.property.md)
  Declares the group of widgets that an app supports.
- [struct WidgetBundleBuilder](widgetbundlebuilder.md)
  A custom attribute that constructs a widget bundle’s body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundle/body-swift.associatedtype)*