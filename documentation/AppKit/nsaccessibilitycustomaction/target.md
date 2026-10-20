# target

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that performs the action through a selector.

**Availability**:
- macOS 10.13+

## Declaration

```swift
weak var target: (any NSObjectProtocol)? { get set }
```

```objc
@property (weak, nullable) id<NSObject> target;
```

## See Also

### Getting the Action
- [var handler: (() -> Bool)?](./handler.md)
  The closure that handles the execution of the action.
- [var selector: Selector?](./selector.md)
  The method to call on the target to perform the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomaction/target)*