# cellClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the type of cell used by the receiver.

**Availability**:
- macOS

## Declaration

```swift
class var cellClass: AnyClass? { get set }
```

```objc
@property (class, nullable) Class cellClass;
```

## Return Value

The class of the cell used to manage the receiver’s contents, or `nil` if no cell class has been set for the receiver or its superclasses (up to NSControl).

## See Also

### Deprecated properties
- [var cell: NSCell?](./cell.md)
  The receiver’s cell object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/cellclass)*