# view(forRow:forComponent:)

**Framework**: UIKit  
**Kind**: method

Returns the view used by the picker view for a given row and component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func view(forRow row: Int, forComponent component: Int) -> UIView?
```

#### Return Value

The view provided by the delegate in the [`pickerView(_:viewForRow:forComponent:reusing:)`](uipickerviewdelegate/pickerview(_:viewforrow:forcomponent:reusing:).md) method. Returns `nil` if the specified row of the component is not visible or if the delegate does not implement p`ickerView:viewForRow:forComponent:reusingView:`.

## Parameters

- `row`: The zero-indexed number of a row of the picker view.
- `component`: The zero-indexed number of a component of the picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/view(forrow:forcomponent:))*