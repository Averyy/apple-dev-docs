# UIPickerViewDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for a picker view’s delegate.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
@MainActor
protocol UIPickerViewDelegate : NSObjectProtocol
```

```objc
@protocol UIPickerViewDelegate <NSObject>
```

#### Overview

The delegate of a [`UIPickerView`](./uipickerview.md) object must adopt this protocol and implement at least some of its methods to provide the picker view with the data it needs to construct itself.

The delegate implements the required methods of this protocol to return height, width, row title, and the view content for the rows in each component. It must also provide the content for each component’s row, either as a string or a view. Typically the delegate implements other optional methods to respond to new selections or deselections of component rows.

See [`UIPickerView`](./uipickerview.md) for a discussion of components, rows, row content, and row selection.

## Topics

### Setting the dimensions of the picker view
- [func pickerView(UIPickerView, rowHeightForComponent: Int) -> CGFloat](./uipickerviewdelegate/pickerview%28_,rowheightforcomponent%29.md)
  Called by the picker view when it needs the row height to use for drawing row content.
- [func pickerView(UIPickerView, widthForComponent: Int) -> CGFloat](./uipickerviewdelegate/pickerview%28_,widthforcomponent%29.md)
  Called by the picker view when it needs the row width to use for drawing row content.
### Setting the content of component rows
- [func pickerView(UIPickerView, titleForRow: Int, forComponent: Int) -> String?](./uipickerviewdelegate/pickerview%28_,titleforrow,forcomponent%29.md)
  Called by the picker view when it needs the title to use for a given row in a given component.
- [func pickerView(UIPickerView, attributedTitleForRow: Int, forComponent: Int) -> NSAttributedString?](./uipickerviewdelegate/pickerview%28_,attributedtitleforrow,forcomponent%29.md)
  Called by the picker view when it needs the styled title to use for a given row in a given component.
- [func pickerView(UIPickerView, viewForRow: Int, forComponent: Int, reusing: UIView?) -> UIView](./uipickerviewdelegate/pickerview%28_,viewforrow,forcomponent,reusing%29.md)
  Called by the picker view when it needs the view to use for a given row in a given component.
### Responding to row selection
- [func pickerView(UIPickerView, didSelectRow: Int, inComponent: Int)](./uipickerviewdelegate/pickerview%28_,didselectrow,incomponent%29.md)
  Called by the picker view when the user selects a row in a component.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [UIPickerViewAccessibilityDelegate](./uipickerviewaccessibilitydelegate.md)

## See Also

### Customizing the picker behavior
- [var delegate: (any UIPickerViewDelegate)?](./uipickerview/delegate.md)
  The delegate for the picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate)*