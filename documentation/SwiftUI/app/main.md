# main()

**Framework**: SwiftUI  
**Kind**: method

Initializes and runs the app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency static func main()
```

#### Discussion

If you precede your [`App`](app.md) conformer’s declaration with the [`@main`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID626) attribute, the system calls the conformer’s `main()` method to launch the app. SwiftUI provides a default implementation of the method that manages the launch process in a platform-appropriate way.

## See Also

- [init()](app/init.md)
  Creates an instance of the app using the body that you define for its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/app/main())*