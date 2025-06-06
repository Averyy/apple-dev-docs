# current

**Framework**: AppKit  
**Kind**: property

The current print operation for this thread.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var current: NSPrintOperation? { get set }
```

#### Return Value

The print operation object, or `nil` if there is no current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/current)*