# target

**Framework**: AppKit  
**Kind**: property

The object that receives the cell’s action messages.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var target: AnyObject? { get set }
```

#### Discussion

The value of this property is the object that implements the selector specified by the [`action`](nscell/action.md) property. Set the value of this property to `nil` to stop the delivery of action messages.

The default value of this property is `nil`. Setting the value of this property raises with [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException). Subclasses are expected to override this property as part of their target/action implementation.

## See Also

- [var action: Selector?](nscell/action.md)
  The action performed by the cell.
- [var isContinuous: Bool](nscell/iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscell/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/target)*