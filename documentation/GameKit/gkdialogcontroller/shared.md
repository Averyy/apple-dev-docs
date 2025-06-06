# shared()

**Framework**: GameKit  
**Kind**: method

Retrieves the shared instance of the dialog controller.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
class func shared() -> GKDialogController
```

#### Return Value

The shared dialog controller.

#### Discussion

You can use the shared dialog controller or create your own [`GKDialogController`](gkdialogcontroller.md) object. For example, you can create separate [`GKDialogController`](gkdialogcontroller.md) objects for different windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/shared())*