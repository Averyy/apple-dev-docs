# init(rootView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hosting controller object that wraps the specified SwiftUI view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init(rootView: Content)
```

#### Return Value

A `UIHostingController` object initialized with the specified SwiftUI view.

## Parameters

- `rootView`: The root view of the SwiftUI view hierarchy that   you want to manage using the hosting view controller.

## See Also

- [init?(coder: NSCoder, rootView: Content)](uihostingcontroller/init(coder:rootview:).md)
  Creates a hosting controller object from an archive and the specified SwiftUI view.
- [init?(coder: NSCoder)](uihostingcontroller/init(coder:).md)
  Creates a hosting controller object from the contents of the specified archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/init(rootview:))*