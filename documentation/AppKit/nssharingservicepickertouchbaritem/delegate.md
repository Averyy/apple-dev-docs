# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the sharing service picker bar item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
weak var delegate: (any NSSharingServicePickerTouchBarItemDelegate)? { get set }
```

```objc
@property (weak) id<NSSharingServicePickerTouchBarItemDelegate> delegate;
```

## See Also

### Setting the delegate
- [protocol NSSharingServicePickerTouchBarItemDelegate](../nssharingservicepickertouchbaritemdelegate.md)
  A protocol that a sharing service picker item delegate uses to provide a list of items eligible for sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritem/delegate)*