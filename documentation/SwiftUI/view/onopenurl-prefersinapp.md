# onOpenURL(prefersInApp:)

**Framework**: SwiftUI  
**Kind**: method

Sets an `OpenURLAction` that prefers opening URL with an in-app browser. It’s equivalent to calling `.onOpenURL(_:)`

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func onOpenURL(prefersInApp: Bool) -> some View
```

#### Discussion

```swift
.onOpenURL { _ in
    .systemAction(prefersInApp: prefersInApp)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onopenurl(prefersinapp:))*