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
weak var delegate: (any INUIEditVoiceShortcutViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<INUIEditVoiceShortcutViewControllerDelegate> delegate;
```

## See Also

### Handling View Controller Events
- [protocol INUIEditVoiceShortcutViewControllerDelegate](../inuieditvoiceshortcutviewcontrollerdelegate.md)
  The protocol an object implements to receive notifications from the view controller that edits or removes a shortcut in Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuieditvoiceshortcutviewcontroller/delegate)*