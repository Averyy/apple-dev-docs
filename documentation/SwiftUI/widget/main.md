# main()

**Framework**: SwiftUI  
**Kind**: method

Initializes and runs the widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency static func main()
```

#### Overview

Because you precede your [`Widget`](widget.md) conformer’s declaration with the [`@main`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID626) attribute, the system calls your widget’s `main()` method to launch the widget. SwiftUI provides a default implementation of the method that manages the launch process in a platform-appropriate way.

## See Also

- [init()](widget/init.md)
  Creates a widget using `body` as its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widget/main())*