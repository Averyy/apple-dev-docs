# present(_:)

**Framework**: GameKit  
**Kind**: method

Presents the dashboard in the window.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func present(_ viewController: any NSViewController & GKViewController) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the dashboard is presented. [`false`](https://developer.apple.com/documentation/swift/false) if an error occurs.

#### Discussion

The dashboard covers the window until the player dismisses it.

## Parameters

- `viewController`: A Game Center view controller that represents the dashboard.

## See Also

- [func dismiss(Any)](gkdialogcontroller/dismiss(_:).md)
  Dismisses the dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/present(_:))*