# shouldCloseDocument

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver necessarily closes the associated document when the window it manages is closed.

**Availability**:
- macOS

## Declaration

```swift
var shouldCloseDocument: Bool { get set }
```

```objc
@property BOOL shouldCloseDocument;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the receiver necessarily closes the associated document when the window it manages is closed, [`false`](../../Swift/false.md) otherwise. The default value is [`false`](../../Swift/false.md).

## See Also

### Closing the Window
- [func close()](./close%28%29.md)
  Closes the window if it was loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/shouldclosedocument)*