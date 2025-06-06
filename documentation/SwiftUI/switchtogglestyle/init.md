# init()

**Framework**: SwiftUI  
**Kind**: init

Creates a switch toggle style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init()
```

#### Discussion

Don’t call this initializer directly. Instead, use the [`switch`](togglestyle/switch.md) static variable to create this style:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.switch)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/switchtogglestyle/init())*