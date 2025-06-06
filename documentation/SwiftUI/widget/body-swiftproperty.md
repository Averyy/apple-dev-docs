# body

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The content and behavior of the widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency var body: Self.Body { get }
```

#### Discussion

For any widgets that you create, provide a computed `body` property that defines the widget as a composition of SwiftUI views.

Swift infers the widget’s [`Body`](scene/body-swift.associatedtype.md) associated type based on the contents of the `body` property.

## See Also

- [associatedtype Body : WidgetConfiguration](widget/body-swift.associatedtype.md)
  The type of configuration representing the content of the widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widget/body-swift.property)*