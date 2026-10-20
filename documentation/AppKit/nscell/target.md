# target

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that receives the cell’s action messages.

**Availability**:
- macOS

## Declaration

```swift
weak var target: AnyObject? { get set }
```

```objc
@property (weak, nullable) id target;
```

#### Discussion

The value of this property is the object that implements the selector specified by the [`action`](./action.md) property. Set the value of this property to `nil` to stop the delivery of action messages.

The default value of this property is `nil`. Setting the value of this property raises with [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md). Subclasses are expected to override this property as part of their target/action implementation.

## See Also

### Managing the Target and Action
- [var action: Selector?](./action.md)
  The action performed by the cell.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./sendaction%28on%29.md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/target)*