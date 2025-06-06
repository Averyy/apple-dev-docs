# body

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The content and behavior of the control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@ControlWidgetConfigurationBuilder
@MainActor @preconcurrency var body: Self.Body { get }
```

#### Discussion

For any controls that you create, provide a computed `body` property that defines the control using some control widget configuration.

Swift infers the control’s [`Body`](controlwidget/body-swift.associatedtype.md) associated type based on the contents of the `body` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidget/body-swift.property)*