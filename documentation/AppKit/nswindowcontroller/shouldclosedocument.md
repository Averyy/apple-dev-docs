# shouldCloseDocument

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the receiver necessarily closes the associated document when the window it manages is closed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var shouldCloseDocument: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the receiver necessarily closes the associated document when the window it manages is closed, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func close()](nswindowcontroller/close.md)
  Closes the window if it was loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/shouldclosedocument)*