# callAsFunction()

**Framework**: SwiftUI  
**Kind**: method

Opens the window associated to the [`Settings`](settings.md) scene defined by this app, if one exists.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction()
```

#### Discussion

Calling this action when the window is already open will order it to the front.

Don’t call this method directly. SwiftUI calls it when you call the [`openSettings`](environmentvalues/opensettings.md) action:

```swift
openSettings()
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/opensettingsaction/callasfunction())*