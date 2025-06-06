# delegate

**Framework**: UIKit  
**Kind**: property

The delegate for the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPickerViewDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`UIPickerViewDelegate`](uipickerviewdelegate.md) protocol and implement the required methods to return the drawing rectangle for rows in each component. It also provides the content for each component’s row, either as a string or a view, and it typically responds to new selections or deselections.

## See Also

- [protocol UIPickerViewDelegate](uipickerviewdelegate.md)
  The interface for a picker view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/delegate)*