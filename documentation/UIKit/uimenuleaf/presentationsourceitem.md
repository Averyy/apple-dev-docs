# presentationSourceItem

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The item you can use as an anchor for subsequent presentations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var presentationSourceItem: (any UIPopoverPresentationControllerSourceItem)? { get }
```

#### Discussion

The system populates this property during the execution of the menu element’s action (its handler or selector). For example, for a menu element in a menu that presents from a [`UIButton`](uibutton.md), the system may populate this property with that button.

Use this property to specify where to anchor popovers when a person taps the menu element, like in the following code.

```swift
let share = UIAction(title: "Share") { [unowned self] action in
    let shareVC = UIActivityViewController(activityItems: items, applicationActivities: activities)
    shareVC.modalPresentationStyle = .popover
    shareVC.popoverPresentationController?.sourceItem = action.presentationSourceItem
    present(shareVC, animated: true)
}
```

## See Also

- [var title: String](uimenuleaf/title.md)
  A short display title for the menu element.
- [var discoverabilityTitle: String?](uimenuleaf/discoverabilitytitle.md)
  A long, informative title to use in the keyboard shortcut overlay.
- [var image: UIImage?](uimenuleaf/image.md)
  An image that appears next to the menu element.
- [var attributes: UIMenuElement.Attributes](uimenuleaf/attributes.md)
  The attributes that determine the style of the menu element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuleaf/presentationsourceitem)*