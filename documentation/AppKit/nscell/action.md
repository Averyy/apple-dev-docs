# action

**Framework**: AppKit  
**Kind**: property

The action performed by the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var action: Selector? { get set }
```

#### Discussion

The value of this property is the selector to call on the cell’s [`target`](nscell/target.md) object. Set the value of this property to `nil` to stop the delivery of action messages.

The default value of this property is `nil`. Setting the value of this property raises with [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException). Subclasses are expected to override this property as part of their target/action implementation.

## See Also

- [var target: AnyObject?](nscell/target.md)
  The object that receives the cell’s action messages.
- [var isContinuous: Bool](nscell/iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscell/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/action)*