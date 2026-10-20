# current

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The current print operation for this thread.

**Availability**:
- macOS

## Declaration

```swift
class var current: NSPrintOperation? { get set }
```

```objc
@property (class, strong, nullable) NSPrintOperation * currentOperation;
```

#### Return Value

The print operation object, or `nil` if there is no current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/current)*