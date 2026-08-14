# isUndoing

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

The value is [`true`](https://developer.apple.com/documentation/swift/true) if the manager is performing its [`undo()`](undomanager/undo().md) or [`undoNestedGroup()`](undomanager/undonestedgroup().md) method, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isRedoing: Bool](undomanager/isredoing.md)
  Returns a Boolean value that indicates whether the manager is in the process of performing a redo action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/isundoing)*