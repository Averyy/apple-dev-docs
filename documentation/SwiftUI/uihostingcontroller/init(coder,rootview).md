# init(coder:rootView:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

- `aDecoder`: The decoder to use during initialization.
- `rootView`: The root view of the SwiftUI view hierarchy that you want to manage using this view controller.

## See Also

### Creating a hosting controller object
- [init(rootView: Content)](./init%28rootview%29.md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a hosting controller object from the contents of the specified archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/init(coder:rootview:))*