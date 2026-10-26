# delegate

**Framework**: IntentsUI  
**Kind**: property  
**Role**: Instance Property

The object that retrieves notifications from the view controller.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any INUIAddVoiceShortcutViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<INUIAddVoiceShortcutViewControllerDelegate> delegate;
```

## See Also

### Handling View Controller Events
- [protocol INUIAddVoiceShortcutViewControllerDelegate](../inuiaddvoiceshortcutviewcontrollerdelegate.md)
  The protocol an object implements to receive notifications from the view controller adding a shortcut to Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutviewcontroller/delegate)*