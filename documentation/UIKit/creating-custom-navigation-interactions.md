# Creating custom navigation interactions

**Framework**: UIKit

Build nonstandard navigation interactions that move focus to the desired location.

#### Overview

For most apps, a simple layout is all that’s needed for the user to interact with your app. However, sometimes the focus engine doesn’t move focus where desired, or doesn’t move focus at all. For these situations, use the [`UIFocusGuide`](uifocusguide.md) class to create invisible regions that redirect focus.

##### Place Your Focusable Items

Place focusable items in your app and arrange them as desired. Where possible, take advantage of the focus engine’s built-in behavior. Use a focus guide only when absolutely necessary. The following image shows a row of three buttons and a column of three buttons. Focus moves automatically between buttons in the same row or column, but the focus engine doesn’t move focus when the user swipes down from Button 2 or Button 3. However, for this layout, the goal is for Button 4 to become focused when the user swipes down.

![Screenshot that shows the creation of a menu layout.](https://docs-assets.developer.apple.com/published/6c248a54cea79794d38a66c9c81372ac/media-2943339%402x.png)

##### Add a Focus Guide

To get focus to move to Button 4 when the user swipes down from Button 2 or Button 3, a focus guide is required. Create a focus guide and add it to the current view. The focus guide is detectable by the focus engine and redirects focus as indicated.

```swift
let myFocusGuide = UIFocusGuide()
self.view.addLayoutGuide(myFocusGuide)
```

##### Add Constraints to the Focus Guide

When the user swipes down from Button 2 or Button 3, the focus should move to Button 4. To make this happen, you need to programmatically add constraints to the focus guide. The focus guide needs to be as wide as Button 2 and Button 3 combined. Set the focus guide’s left constraint to Button 2’s left constraint and its right constraint to Button 3’s right constraint. For convenience, this example sets the focus guide’s top and bottom constraints to Button 4’s top and bottom constraints. Finally, the [`preferredFocusEnvironments`](uifocusguide/preferredfocusenvironments.md) property is set to Button 4. The following image shows the location and size of the focus guide created using the constraints in the following code.

```swift
myFocusGuide.leftAnchor.constraint(equalTo: button_2.leftAnchor).isActive = true
myFocusGuide.rightAnchor.constraint(equalTo: button_3.rightAnchor).isActive = true
myFocusGuide.topAnchor.constraint(equalTo: button_4.topAnchor).isActive = true
myFocusGuide.bottomAnchor.constraint(equalTo: button_4.bottomAnchor).isActive = true
myFocusGuide.preferredFocusEnvironments = [button_4]
```

> **Note**:  The focus guide won’t work if the constraints are set to Active.

 The focus guide won’t work if the constraints are set to Active.

![Screenshot that shows a newly created focus guide.](https://docs-assets.developer.apple.com/published/c7c2a2af4b13e1f40248624d43042691/media-2943334%402x.png)

When users swipe down from Button 2 or Button 3, focus correctly redirects to Button 4.

![Screenshot that shows focus redirecting to Button 4.](https://docs-assets.developer.apple.com/published/7a5d92ec8be8fd144426d65574dd3301/media-2943338%402x.png)

## See Also

- [class UIFocusGuide](uifocusguide.md)
  An object that exposes nonview areas as focusable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/creating-custom-navigation-interactions)*