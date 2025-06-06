# backButtonTitle

**Framework**: UIKit  
**Kind**: property

The custom title of the Back button.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backButtonTitle: String? { get set }
```

#### Discussion

Use this property to set the title of the Back button when a view controller’s [`navigationItem`](uiviewcontroller/navigationitem.md) is the [`backItem`](uinavigationbar/backitem.md) of the navigation bar, in other words, when the Back button appears in the navigation bar of the next view controller. For example, a view controller that displays a list of contacts can set [`backButtonTitle`](uinavigationitem/backbuttontitle.md) to “Contacts”. When a person taps a contact, the view controller pushes a new view controller onto the navigation stack, which displays the details of the selected contact. This new topmost view controller shows “Contacts” as the Back button title.

Interface Builder shows this behavior when setting the Back button title in a storyboard, as shown in the following screenshot:

![A screenshot of Interface Builder displaying a storyboard. The storyboard shows three controllers, a navigation controller connected to a view controller that is connected to a second view controller. The first view controller shows its navigation item as selected. The Attributes inspector shows the properties of the selected navigation item, with “Contacts” highlighted in the Back Button field. The second view controller displays a Back button with the title “Contacts” in its navigation bar.](https://docs-assets.developer.apple.com/published/a03be92bea304f8275e089d0a7d85f0e/media-3901286%402x.png)

When setting [`backButtonTitle`](uinavigationitem/backbuttontitle.md) programmatically, set it in the current view controller before pushing a new view controller onto the navigation stack; for instance, in [`viewDidLoad()`](uiviewcontroller/viewdidload().md) or [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md).

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    navigationItem.backButtonTitle = "Contacts"
}
```

When [`backButtonTitle`](uinavigationitem/backbuttontitle.md) is `nil`, which is the default value, the navigation item uses its [`title`](uinavigationitem/title.md) property as the Back button title.

> **Note**:  [`backBarButtonItem`](uinavigationitem/backbarbuttonitem.md) takes precedence if you specify both [`backButtonTitle`](uinavigationitem/backbuttontitle.md) and [`backBarButtonItem`](uinavigationitem/backbarbuttonitem.md).

 [`backBarButtonItem`](uinavigationitem/backbarbuttonitem.md) takes precedence if you specify both [`backButtonTitle`](uinavigationitem/backbuttontitle.md) and [`backBarButtonItem`](uinavigationitem/backbarbuttonitem.md).

## See Also

- [var backBarButtonItem: UIBarButtonItem?](uinavigationitem/backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
- [var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.property.md)
  The display mode of the Back button.
- [UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.enum.md)
  Constants that describe the display modes of the Back button.
- [var hidesBackButton: Bool](uinavigationitem/hidesbackbutton.md)
  A Boolean value that determines whether the navigation item hides the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](uinavigationitem/sethidesbackbutton(_:animated:).md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](uinavigationitem/backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttontitle)*