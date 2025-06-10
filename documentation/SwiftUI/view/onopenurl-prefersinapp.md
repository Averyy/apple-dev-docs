# onOpenURL(prefersInApp:)

**Framework**: SwiftUI  
**Kind**: method

Sets an `OpenURLAction` that prefers opening URL with an in-app browser. It’s equivalent to calling `.onOpenURL(_:)`

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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