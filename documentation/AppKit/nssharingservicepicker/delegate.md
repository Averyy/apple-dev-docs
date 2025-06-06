# delegate

**Framework**: AppKit  
**Kind**: property

The object for managing the sharing service picker.

**Availability**:
- macOS 10.8+

## Declaration

```swift
weak var delegate: (any NSSharingServicePickerDelegate)? { get set }
```

#### Discussion

The delegate object must conform to the [`NSSharingServicePickerDelegate`](nssharingservicepickerdelegate.md) delegate.

## See Also

- [protocol NSSharingServicePickerDelegate](nssharingservicepickerdelegate.md)
  An interface for managing content for the macOS share sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/delegate)*