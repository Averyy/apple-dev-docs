# init()

**Framework**: SwiftUI  
**Kind**: init

Creates a checkbox toggle style.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init()
```

#### Discussion

Don’t call this initializer directly. Instead, use the [`checkbox`](togglestyle/checkbox.md) static variable to create this style:

```swift
Toggle("Close windows when quitting an app", isOn: $doesClose)
    .toggleStyle(.checkbox)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/checkboxtogglestyle/init())*