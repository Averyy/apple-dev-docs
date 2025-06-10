# localObject

**Framework**: UIKit  
**Kind**: property

A custom object associated with the drag item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var localObject: Any? { get set }
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)
- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

#### Discussion

The `localObject` property gives you the option to associate a custom object, such as a model object, with the drag item. The local object is available only to the app that initiates the drag activity.

## See Also

- [var itemProvider: NSItemProvider](uidragitem/itemprovider.md)
  The item provider associated with the drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragitem/localobject)*