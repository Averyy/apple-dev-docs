# action

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The action sent to the first responder when the user selects a new font from the Font panel or chooses a command from the Font menu.

**Availability**:
- macOS

## Declaration

```swift
var action: Selector { get set }
```

```objc
@property SEL action;
```

## Discussion

The default action is [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md). You should rarely need to change this setting.

## See Also

### Accessing the Action Property
- [var target: AnyObject?](./target.md)
  The object that receives action messages related to the font manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/action)*