# init(coder:rootView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hosting controller object from an archive and the specified SwiftUI view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init?(coder aDecoder: NSCoder, rootView: Content)
```

#### Return Value

A `UIViewController` object that you can present from your interface.

## Parameters

- `rootView`: The root view of the SwiftUI view hierarchy that you want   to manage using this view controller.

## See Also

- [init(rootView: Content)](uihostingcontroller/init(rootview:).md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder)](uihostingcontroller/init(coder:).md)
  Creates a hosting controller object from the contents of the specified archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/init(coder:rootview:))*