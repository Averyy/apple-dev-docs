# Getting the user’s attention with alerts and action sheets

**Framework**: UIKit

Present important information to the user or prompt the user about an important choice.

#### Overview

Display an alert or action sheet when your app requires additional information or acknowledgment from the user. Alerts and action sheets interrupt your app’s normal flow to display a message to the user. In the following image, the left image shows an alert and the right image shows an action sheet. The user dismisses an alert or action sheet by selecting one of the listed options.

![An alert shows location services are off. An action sheet from Safari asks what to do with tabs.](https://docs-assets.developer.apple.com/published/f9d8686737bb1cb4a4a13ec0a93a8453/media-2938395%402x.png)

> ❗ **Important**:  Because alerts and action sheets are an interruption, use them sparingly and only when absolutely needed. For detailed guidance on when to use them, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/all-components).

 Because alerts and action sheets are an interruption, use them sparingly and only when absolutely needed. For detailed guidance on when to use them, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/all-components).

To display an alert or action sheet, create a [`UIAlertController`](uialertcontroller.md) object, configure it, and call its [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method, as shown in the following code. Configuring the alert controller includes specifying the title and message that you want the user to see and the actions the user can select. You must add at least one action — represented by a [`UIAlertAction`](uialertaction.md) object — to an alert controller before presenting it.

```swift
@IBAction func agreeToTerms() {
   // Create the action buttons for the alert.
   let defaultAction = UIAlertAction(title: "Agree", 
                        style: .default) { (action) in
	// Respond to user selection of the action.
   }
   let cancelAction = UIAlertAction(title: "Disagree", 
                        style: .cancel) { (action) in
	// Respond to user selection of the action.
   }
   
   // Create and configure the alert controller.     
   let alert = UIAlertController(title: "Terms and Conditions",
         message: "Click Agree to accept the terms and conditions.",
         preferredStyle: .alert)
   alert.addAction(defaultAction)
   alert.addAction(cancelAction)
        
   self.present(alert, animated: true) {
      // The alert was presented
   }
}
```

##### Present an Action Sheet on Ipad

On iPad, UIKit requires that you display an action sheet inside a popover. The following image shows an action sheet anchored to a bar button item.

![On iPad, an action sheet is anchored to a bar button item in a toolbar.](https://docs-assets.developer.apple.com/published/e159e6db3f6e8028c8f828861797ab16/media-2940105%402x.png)

To display your action sheet in a popover, specify your popover’s anchor point using the [`popoverPresentationController`](uiviewcontroller/popoverpresentationcontroller.md) property of your alert controller. It’s safe to configure this property regardless of the underlying device. In other words, The following code displays the action sheet in a popover on iPad and as a slide-up presentation on iPhone.

```swift
@IBAction func deleteItem() {
   let destroyAction = UIAlertAction(title: "Delete", 
             style: .destructive) { (action) in
	// Respond to user selection of the action
   }
   let cancelAction = UIAlertAction(title: "Cancel", 
             style: .cancel) { (action) in
	// Respond to user selection of the action
   }
        
   let alert = UIAlertController(title: "Delete the image?", 
               message: "", 
               preferredStyle: .actionSheet)
   alert.addAction(destroyAction)
   alert.addAction(cancelAction)
        
   // On iPad, action sheets must be presented from a popover.
   alert.popoverPresentationController?.barButtonItem = 
               self.trashButton
        
   self.present(alert, animated: true) {
      // The alert was presented
   }
}
```

> **Note**:  If your set of actions includes a button configured with the [`UIAlertAction.Style.cancel`](uialertaction/style-swift.enum/cancel.md) style, UIKit removes that button when displaying your action sheet in a popover. Tapping anywhere outside of the popover has the same effect as tapping the Cancel button, including calling your action handler.

 If your set of actions includes a button configured with the [`UIAlertAction.Style.cancel`](uialertaction/style-swift.enum/cancel.md) style, UIKit removes that button when displaying your action sheet in a popover. Tapping anywhere outside of the popover has the same effect as tapping the Cancel button, including calling your action handler.

## See Also

- [class UIAlertController](uialertcontroller.md)
  An object that displays an alert message.
- [class UIAlertAction](uialertaction.md)
  An action that can be taken when the user taps a button in an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/getting-the-user-s-attention-with-alerts-and-action-sheets)*