# init(coder:rootView:)

**Framework**: SwiftUI  
**Kind**: init

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
- `rootView`: The root view of the SwiftUI view hierarchy that you want   to manage using this view controller.

## See Also

- [init(rootView: Content)](nshostingcontroller/init(rootview:).md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder)](nshostingcontroller/init(coder:).md)
  Creates a hosting controller object from the contents of the specified archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingcontroller/init(coder:rootview:))*