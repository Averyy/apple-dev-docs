# selector

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The method to call on the target to perform the action.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var selector: Selector? { get set }
```

```objc
@property (nullable) SEL selector;
```

## See Also

### Getting the Action
- [var handler: (() -> Bool)?](./handler.md)
  The closure that handles the execution of the action.
- [var target: (any NSObjectProtocol)?](./target.md)
  The object that performs the action through a selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomaction/selector)*