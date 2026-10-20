# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate associated with the date picker.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSDatePickerCellDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSDatePickerCellDelegate> delegate;
```

#### Discussion

The delegate must conform to [`NSDatePickerCellDelegate`](../nsdatepickercelldelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/delegate)*