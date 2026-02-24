# onOpenURL(prefersInApp:)

**Framework**: SwiftUI  
**Kind**: method

Sets an `OpenURLAction` that prefers opening URL with an in-app browser. The `handler` closure takes a URL as input, and returns a `OpenURLAction.Result` that indicates the outcome of the action.

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

It’s equivalent to calling `.onOpenURL(_:)`

```swift
.onOpenURL { _ in
    .systemAction(prefersInApp: prefersInApp)
}
```

## Parameters

- `prefersInApp`: A boolean value that specifies whether to prefer to open the URL with an in-app browser or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onopenurl(prefersinapp:))*