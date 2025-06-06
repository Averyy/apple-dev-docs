# delegate

**Framework**: AppKit  
**Kind**: property

The object that acts as the delegate of the sharing service picker bar item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
weak var delegate: (any NSSharingServicePickerTouchBarItemDelegate)? { get set }
```

## See Also

- [protocol NSSharingServicePickerTouchBarItemDelegate](nssharingservicepickertouchbaritemdelegate.md)
  A protocol that a sharing service picker item delegate uses to provide a list of items eligible for sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritem/delegate)*