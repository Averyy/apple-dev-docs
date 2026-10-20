# init(coder:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hosting controller object from the contents of the specified archive.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency required dynamic init?(coder aDecoder: NSCoder)
```

#### Discussion

The default implementation of this method throws an exception. To create your view controller from an archive, override this method and initialize the superclass using the [`init(coder:rootView:)`](uihostingcontroller/init(coder:rootview:).md) method instead.

-Parameter coder: The decoder to use during initialization.

## See Also

- [init(rootView: Content)](uihostingcontroller/init(rootview:).md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder, rootView: Content)](uihostingcontroller/init(coder:rootview:).md)
  Creates a hosting controller object from an archive and the specified SwiftUI view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/init(coder:))*