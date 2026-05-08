# init()

**Framework**: SwiftUI  
**Kind**: init

Creates a button toggle style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init()
```

#### Discussion

Don’t call this initializer directly. Instead, use the [`button`](togglestyle/button.md) static variable to create this style:

```swift
Toggle(isOn: $isFlagged) {
    Label("Flag", systemImage: "flag.fill")
}
.toggleStyle(.button)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttontogglestyle/init())*