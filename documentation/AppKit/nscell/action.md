# action

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The action performed by the cell.

**Availability**:
- macOS

## Declaration

```swift
var action: Selector? { get set }
```

```objc
@property (nullable) SEL action;
```

#### Discussion

The value of this property is the selector to call on the cell’s [`target`](./target.md) object. Set the value of this property to `nil` to stop the delivery of action messages.

The default value of this property is `nil`. Setting the value of this property raises with [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md). Subclasses are expected to override this property as part of their target/action implementation.

## See Also

### Managing the Target and Action
- [var target: AnyObject?](./target.md)
  The object that receives the cell’s action messages.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether the cell sends its action message continuously during mouse tracking.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](./sendaction%28on%29.md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/action)*