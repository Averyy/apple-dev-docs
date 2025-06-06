# init(_:)

**Framework**: Swiftui  
**Kind**: init

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application Delegate.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

#### Discussion

The framework will initialize the provided delegate and manage its lifetime, calling out to it when appropriate after performing its own work.

> **Note**: The instantiated delegate will be placed in the Environment and may be accessed by using the `@Environment` property wrapper in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor/init(_:))*