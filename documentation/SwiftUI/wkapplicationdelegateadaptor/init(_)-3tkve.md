# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application Delegate.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

**Other overloads**:

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

```swift
@MainActor
@preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

## Discussion

The framework will initialize the provided delegate and manage its lifetime, calling out to it when appropriate after performing its own work.

## Parameters

- `delegateType`: The type of `WKApplicationDelegate` to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor/init(_:)-3tkve)*