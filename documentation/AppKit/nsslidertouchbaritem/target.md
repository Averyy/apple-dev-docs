# target

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An object that is notified when a user interacts with the slider or either of the accessories.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
weak var target: AnyObject? { get set }
```

```objc
@property (weak, nullable) id target;
```

## See Also

### Handling slider interaction
- [var action: Selector?](./action.md)
  The selector on the target object that is invoked when a user interacts with the slider or either of the accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidertouchbaritem/target)*