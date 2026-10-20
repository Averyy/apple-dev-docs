# target

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The target object that receives action messages from the stepper.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
weak var target: AnyObject? { get set }
```

```objc
@property (weak, nullable) id target;
```

## See Also

### Handling stepper interaction
- [var action: Selector?](./action.md)
  The action-message selector associated with the stepper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppertouchbaritem/target)*