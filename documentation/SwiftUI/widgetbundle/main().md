# main()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Initializes and runs the widget bundle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency static func main()
```

#### Overview

Because you precede your [`WidgetBundle`](../widgetbundle.md) conformer’s declaration with the [@main](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID626) attribute, the system calls your widget bundle’s `main()` method to launch the widget bundle. SwiftUI provides a default implementation of the method that manages the launch process in a platform-appropriate way.

## See Also

### Running a widget bundle
- [init()](./init%28%29.md)
  Creates a widget bundle using the bundle’s body as its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundle/main())*