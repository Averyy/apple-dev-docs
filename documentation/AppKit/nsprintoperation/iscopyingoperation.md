# isCopyingOperation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the print operation is an EPS or PDF copy operation.

**Availability**:
- macOS

## Declaration

```swift
var isCopyingOperation: Bool { get }
```

```objc
@property (readonly, getter=isCopyingOperation) BOOL copyingOperation;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver is an EPS or PDF copy operation; otherwise, [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/iscopyingoperation)*