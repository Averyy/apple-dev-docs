# init(coder:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hosting view object from the contents of the specified archive.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency required dynamic init?(coder aDecoder: NSCoder)
```

#### Discussion

The default implementation of this method throws an exception. To create your view from an archive, override this method and initialize the superclass using the [`init(coder:rootView:)`](nshostingview/init(coder:rootview:).md) method instead.

## See Also

- [init(rootView: Content)](nshostingview/init(rootview:).md)
  Creates a hosting view object that wraps the specified SwiftUI view.
- [func prepareForReuse()](nshostingview/prepareforreuse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/init(coder:))*