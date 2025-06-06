# init(rootView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hosting view object that wraps the specified SwiftUI view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency required init(rootView: Content)
```

## Parameters

- `rootView`: The root view of the SwiftUI view hierarchy that   you want to manage using this hosting view.

## See Also

- [init?(coder: NSCoder)](nshostingview/init(coder:).md)
  Creates a hosting view object from the contents of the specified archive.
- [func prepareForReuse()](nshostingview/prepareforreuse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/init(rootview:))*