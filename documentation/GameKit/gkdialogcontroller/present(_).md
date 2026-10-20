# present(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Presents the dashboard in the window.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func present(_ viewController: any NSViewController & GKViewController) -> Bool
```

```objc
- (BOOL) presentViewController:(NSViewController<GKViewController> *) viewController;
```

#### Return Value

[`true`](../../Swift/true.md) if the dashboard is presented. [`false`](../../Swift/false.md) if an error occurs.

#### Discussion

The dashboard covers the window until the player dismisses it.

## Parameters

- `viewController`: A Game Center view controller that represents the dashboard.

## See Also

### Presenting and Dismissing the Dialog
- [func dismiss(Any)](./dismiss%28_%29.md)
  Dismisses the dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/present(_:))*