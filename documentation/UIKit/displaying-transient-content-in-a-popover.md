# Displaying transient content in a popover

**Framework**: UIKit

Show a temporary interface on top of your app’s content on iPad.

#### Overview

Use popovers for app content that appears when needed and disappears when the user is finished with it. For example, use popovers to display information about the currently selected item, to display tools and configuration options, or to gather information from the user. You anchor a popover to a specific location onscreen, and the popover floats above the main window. The following image shows how the Calendar app on iPad uses a popover to prompt the user for new meeting information.

![Calendar uses a popover to display the interface for creating new events.](https://docs-assets.developer.apple.com/published/f426b98e953dbb4179c00da7dbde013e/media-2938388%402x.png)

You specify the content of a popover using a view controller. You then present your view controller using the popover presentation style. UIKit anchors your popover to the location you specify.

The following code shows how to present a popover from a bar button item, which acts as the anchor point for the popover. UIKit uses the position of that bar button item to determine where to place the popover and how to orient its arrow. The view controller’s [`UIPopoverPresentationController`](uipopoverpresentationcontroller.md) manages the display of your popover onscreen.

```swift
@IBAction func displayOptionsForSelectedItem () {
   // Load and configure your view controller.
   let storyboard = UIStoryboard(name: "Main", bundle: nil)
   let optionsVC = storyboard.instantiateViewController( 
              withIdentifier: "itemOptionsViewController")
    
   // Use the popover presentation style for your view controller.    
   optionsVC.modalPresentationStyle = .popover

   // Specify the anchor point for the popover.
   optionsVC.popoverPresentationController?.barButtonItem = 
              optionsControl

   // Present the view controller (in a popover).
   self.present(optionsVC, animated: true) {
      // The popover is visible.
   }
}
```

Configure other properties of your view controller’s [`UIPopoverPresentationController`](uipopoverpresentationcontroller.md) object before calling the [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method. For example, you might want to assign a delegate to manage the presentation and dismissal of the popover.

## See Also

- [class UIPopoverPresentationController](uipopoverpresentationcontroller.md)
  An object that manages the display of content in a popover.
- [class UIPopoverBackgroundView](uipopoverbackgroundview.md)
  The background appearance for a popover.
- [protocol UIPopoverBackgroundViewMethods](uipopoverbackgroundviewmethods.md)
  A set of methods that popover background view subclasses must implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/displaying-transient-content-in-a-popover)*