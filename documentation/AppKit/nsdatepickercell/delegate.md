# delegate

**Framework**: AppKit  
**Kind**: property

The delegate associated with the date picker.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var delegate: (any NSDatePickerCellDelegate)? { get set }
```

#### Discussion

The delegate must conform to [`NSDatePickerCellDelegate`](nsdatepickercelldelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/delegate)*