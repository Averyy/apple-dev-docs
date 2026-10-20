# init(coder:rootView:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a hosting controller object from an archive and the specified SwiftUI view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency init?(coder: NSCoder, rootView: Content)
```

## Parameters

- `coder`: The decoder to use during initialization.
- `rootView`: The root view of the SwiftUI view hierarchy that you want to manage using this view controller.

## See Also

### Creating a hosting controller object
- [init(rootView: Content)](./init%28rootview%29.md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a hosting controller object from the contents of the specified archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingcontroller/init(coder:rootview:))*