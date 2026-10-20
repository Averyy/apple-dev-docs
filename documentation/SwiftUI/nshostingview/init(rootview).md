# init(rootView:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a hosting view object that wraps the specified SwiftUI view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency required init(rootView: Content)
```

## Parameters

- `rootView`: The root view of the SwiftUI view hierarchy that you want to manage using this hosting view.

## See Also

### Creating a hosting view
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a hosting view object from the contents of the specified archive.
- [func prepareForReuse()](./prepareforreuse%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/init(rootview:))*