# isUndoing

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the manager is in the process of performing an undo action.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isUndoing: Bool { get }
```

```objc
@property (readonly, getter=isUndoing) BOOL undoing;
```

#### Discussion

The value is [`true`](../../Swift/true.md) if the manager is performing its [`undo()`](./undo%28%29.md) or [`undoNestedGroup()`](./undonestedgroup%28%29.md) method, otherwise [`false`](../../Swift/false.md).

## See Also

### Checking whether undo or redo is in process
- [var isRedoing: Bool](./isredoing.md)
  Returns a Boolean value that indicates whether the manager is in the process of performing a redo action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/isundoing)*