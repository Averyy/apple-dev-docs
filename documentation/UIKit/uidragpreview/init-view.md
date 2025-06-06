# init(view:)

**Framework**: UIKit  
**Kind**: init

Initializes a new drag item preview with a view, using the default appearance parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(view: UIView)
```

#### Return Value

A drag preview that is based on the specified view.

#### Discussion

Use this method to display a drag item preview based on a view that you provide. The preview displays a snapshot of the provided view. Changes to the view don’t appear after the preview is shown, and the preview doesn’t change or move the view.

## Parameters

- `view`: A   object representing the drag item.

## See Also

- [init(view: UIView, parameters: UIDragPreviewParameters)](uidragpreview/init(view:parameters:).md)
  Initializes a new drag item preview with a view and with a set of appearance parameters.
- [convenience init(forURL: URL)](uidragpreview/init(forurl:).md)
  Initializes a new drag item preview with a URL.
- [convenience init(forURL: URL, title: String?)](uidragpreview/init(forurl:title:).md)
  Initializes a drag item preview with a URL and title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreview/init(view:))*