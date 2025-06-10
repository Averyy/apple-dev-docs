# onOpenURL(prefersInApp:)

**Framework**: DeviceActivity  
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

## Parameters

- `handler`: The closure to run for the given URL.   The closure takes a URL as input, and returns a    that indicates the outcome of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/onopenurl(prefersinapp:))*