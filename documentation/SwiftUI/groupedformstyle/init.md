# init()

**Framework**: SwiftUI  
**Kind**: init

Creates a form style with scrolling, grouped rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init()
```

#### Discussion

Don’t call this initializer directly. Instead, use the [`grouped`](formstyle/grouped.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.grouped)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupedformstyle/init())*