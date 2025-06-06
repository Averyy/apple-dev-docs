# init(coder:rootView:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hosting view object from an archive and the specified SwiftUI view.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
@preconcurrency init?(coder: NSCoder, rootView: Content)
```

## Parameters

- `coder`: The decoder to use during initialization.
- `rootView`: The root view of the SwiftUI view hierarchy that   you want to manage using this hosting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/init(coder:rootview:))*