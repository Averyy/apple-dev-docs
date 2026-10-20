# homeEmbeddedNavigationDestination(for:destination:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Drop-in replacement for `.navigationDestination(for:)` for hosted extension content. Pair with `context.navigator.push(_:title:)` or `NavigationLink(value:)`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func homeEmbeddedNavigationDestination<D, Content>(for data: D.Type, @ContentBuilder destination: @escaping (D) -> Content) -> some View where D : Hashable, Content : View
```

#### Discussion

```swift
// On your root view, register how each pushed route builds its view:
MyRootView()
    .homeEmbeddedNavigationDestination(for: Route.self) { route in
        switch route {
        case .schedule: ScheduleView()
        }
    }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/homeembeddednavigationdestination(for:destination:))*