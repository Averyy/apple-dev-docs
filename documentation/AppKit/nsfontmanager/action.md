# action

**Framework**: AppKit  
**Kind**: property

The action sent to the first responder when the user selects a new font from the Font panel or chooses a command from the Font menu.

**Availability**:
- macOS ?+

## Declaration

```swift
var action: Selector { get set }
```

#### Discussion

The default action is [`changeFont:`](https://developer.apple.com/documentation/objectivec/nsobject/1462311-changefont). You should rarely need to change this setting.

## See Also

- [var target: AnyObject?](nsfontmanager/target.md)
  The object that receives action messages related to the font manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/action)*