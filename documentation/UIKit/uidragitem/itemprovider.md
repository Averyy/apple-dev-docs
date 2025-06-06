# itemProvider

**Framework**: UIKit  
**Kind**: property

The item provider associated with the drag item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var itemProvider: NSItemProvider { get }
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)
- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Discussion

The item provider conveys the data, or file, that the drag-and-drop activity shares between processes. The property is set when the [`UIDragItem`](uidragitem.md) instance is created. For more information, see [`init(itemProvider:)`](uidragitem/init(itemprovider:).md).

## See Also

- [var localObject: Any?](uidragitem/localobject.md)
  A custom object associated with the drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragitem/itemprovider)*