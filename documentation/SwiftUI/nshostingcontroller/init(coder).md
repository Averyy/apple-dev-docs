# init(coder:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a hosting controller object from the contents of the specified archive.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency required dynamic init?(coder: NSCoder)
```

## Discussion

The default implementation of this method throws an exception. To create your view controller from an archive, override this method and initialize the superclass using the [`init(coder:rootView:)`](./init%28coder,rootview%29.md) method instead.

## Parameters

- `coder`: The decoder to use during initialization.

## See Also

### Creating a hosting controller object
- [init(rootView: Content)](./init%28rootview%29.md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder, rootView: Content)](./init%28coder,rootview%29.md)
  Creates a hosting controller object from an archive and the specified SwiftUI view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingcontroller/init(coder:))*