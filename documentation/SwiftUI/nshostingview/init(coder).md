# init(coder:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a hosting view object from the contents of the specified archive.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency required dynamic init?(coder aDecoder: NSCoder)
```

## Discussion

The default implementation of this method throws an exception. To create your view from an archive, override this method and initialize the superclass using the [`init(coder:rootView:)`](./init%28coder,rootview%29.md) method instead.

## Parameters

- `aDecoder`: The decoder to use during initialization.

## See Also

### Creating a hosting view
- [init(rootView: Content)](./init%28rootview%29.md)
  Creates a hosting view object that wraps the specified SwiftUI view.
- [func prepareForReuse()](./prepareforreuse%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/init(coder:))*