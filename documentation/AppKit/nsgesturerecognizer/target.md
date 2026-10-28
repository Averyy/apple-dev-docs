# target

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that implements the action method.

**Availability**:
- macOS 10.10+

## Declaration

```swift
weak var target: AnyObject? { get set }
```

```objc
@property (weak, nullable) id target;
```

## Discussion

The object in this property must implement the method specified by the [`action`](./action.md) property.

## See Also

### Accessing the target and action
- [var action: Selector?](./action.md)
  The action method to call when the gesture is recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/target)*