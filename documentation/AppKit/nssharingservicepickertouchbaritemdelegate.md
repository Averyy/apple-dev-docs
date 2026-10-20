# NSSharingServicePickerTouchBarItemDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that a sharing service picker item delegate uses to provide a list of items eligible for sharing.

**Availability**:
- macOS

## Declaration

```swift
protocol NSSharingServicePickerTouchBarItemDelegate : NSSharingServicePickerDelegate
```

```objc
@protocol NSSharingServicePickerTouchBarItemDelegate <NSSharingServicePickerDelegate>
```

## Topics

### Providing items to share
- [func items(for: NSSharingServicePickerTouchBarItem) -> [Any]](./nssharingservicepickertouchbaritemdelegate/items%28for%29.md)
  Asks the delegate for items that represent the objects to be shared.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSharingServicePickerDelegate](./nssharingservicepickerdelegate.md)

## See Also

### Setting the delegate
- [var delegate: (any NSSharingServicePickerTouchBarItemDelegate)?](./nssharingservicepickertouchbaritem/delegate.md)
  The object that acts as the delegate of the sharing service picker bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritemdelegate)*