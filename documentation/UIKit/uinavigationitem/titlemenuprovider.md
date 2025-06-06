# titleMenuProvider

**Framework**: UIKit  
**Kind**: property

A closure that generates the navigation item’s title menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var titleMenuProvider: (([UIMenuElement]) -> UIMenu?)? { get set }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

UIKit calls this closure to create a context menu that appears when a person taps the title of the navigation item. UIKit passes in a set of menu element suggestions that you can either use directly or modify in this closure to customize the menu.

```swift
// Use suggested menu elements directly.
navigationItem.titleMenuProvider = { suggestions in
    return UIMenu(children: suggestions)
}

// Add a custom menu element to the suggestions.
navigationItem.titleMenuProvider = { suggestions in
    var finalMenuElements = suggestions
    finalMenuElements.append(UICommand(title: "Save", 
                                       image: UIImage(systemName: "square.and.arrow.down"), 
                                      action: #selector(self.save)))
    return UIMenu(children: finalMenuElements)
}
```

Before displaying the title menu, UIKit validates each element in the menu you return by traversing the responder chain, starting with the navigation controller’s [`topViewController`](uinavigationcontroller/topviewcontroller.md). For selector-based menu elements, implement your methods on [`topViewController`](uinavigationcontroller/topviewcontroller.md) or farther up in the responder chain if you want those elements to appear in the title menu. For more information, see [`canPerformAction(_:withSender:)`](uiresponder/canperformaction(_:withsender:).md).

> 💡 **Tip**:  You don’t need to assign a [`titleMenuProvider`](uinavigationitem/titlemenuprovider.md) if you only want to show Rename in your title menu. If you assign a `renameDelegate` without setting a [`titleMenuProvider`](uinavigationitem/titlemenuprovider.md), UIKit automatically generates a title menu containing the Rename menu element only.

 You don’t need to assign a [`titleMenuProvider`](uinavigationitem/titlemenuprovider.md) if you only want to show Rename in your title menu. If you assign a `renameDelegate` without setting a [`titleMenuProvider`](uinavigationitem/titlemenuprovider.md), UIKit automatically generates a title menu containing the Rename menu element only.

## See Also

- [var documentProperties: UIDocumentProperties?](uinavigationitem/documentproperties.md)
  An object that provides the document header for the title menu.
- [class UIDocumentProperties](uidocumentproperties.md)
  Information that UIKit uses to generate a document header for a navigation item’s title menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlemenuprovider)*