# customActions

**Framework**: UIKit  
**Kind**: property

Custom document browser actions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var customActions: [UIDocumentBrowserAction] { get set }
```

## Mentions

- [Adding custom actions and activities](adding-custom-actions-and-activities.md)

#### Discussion

By default, this property contains an empty array. Assign an array of [`UIDocumentBrowserAction`](uidocumentbrowseraction.md) objects to add custom document browser actions.

Document browser actions can be accessed in two ways:

-  actions appear in the Navigation bar when the user places the browser into the Select mode.
-  actions appear when the user long presses on a document or folder.

When triggered, these actions are passed the URLs of the currently selected items.

## See Also

- [class UIDocumentBrowserAction](uidocumentbrowseraction.md)
  A custom action that you can create and add to a document browser’s Edit menu or navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/customactions)*