# isRedoing

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the manager is in the process of performing a redo action.

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
var isRedoing: Bool { get }
```

```objc
@property (readonly, getter=isRedoing) BOOL redoing;
```

## Discussion

The value is [`true`](../../Swift/true.md) if the manager is performing its [`redo()`](./redo%28%29.md) method, otherwise [`false`](../../Swift/false.md).

## See Also

### Checking whether undo or redo is in process
- [var isUndoing: Bool](./isundoing.md)
  Returns a Boolean value that indicates whether the manager is in the process of performing an undo action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/isredoing)*