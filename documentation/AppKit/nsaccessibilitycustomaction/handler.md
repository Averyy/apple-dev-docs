# handler

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The closure that handles the execution of the action.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var handler: (() -> Bool)? { get set }
```

```objc
@property (copy, nullable) BOOL (^handler)();
```

## See Also

### Getting the Action
- [var target: (any NSObjectProtocol)?](./target.md)
  The object that performs the action through a selector.
- [var selector: Selector?](./selector.md)
  The method to call on the target to perform the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomaction/handler)*