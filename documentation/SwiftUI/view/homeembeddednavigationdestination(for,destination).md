# homeEmbeddedNavigationDestination(for:destination:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Defines the view to display when your extension pushes a value of the given type.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Declaration

```swift
@MainActor
@preconcurrency func homeEmbeddedNavigationDestination<D, Content>(for data: D.Type, @ContentBuilder destination: @escaping (D) -> Content) -> some View where D : Hashable, Content : View
```

## Return Value

A view that handles navigation for the given type.

## Discussion

Use this modifier instead of `navigationDestination(for:destination:)` in your extension’s content. It works with both `HomeNavigator/push(_:title:)` and value-based navigation links.

For example, to register destinations on your root view:

```swift
MyRootView()
    .homeEmbeddedNavigationDestination(for: Route.self) { route in
        switch route {
        case .schedule: ScheduleView()
        }
    }
```

## Parameters

- `data`: The type of value this destination handles.
- `destination`: A view builder that creates the view for a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/homeembeddednavigationdestination(for:destination:))*