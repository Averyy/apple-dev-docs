# init(forURL:title:)

**Framework**: UIKit  
**Kind**: init

Initializes a drag item preview with a URL and title.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
convenience init(for url: URL, title: String?)
```

#### Return Value

A drag preview for a URL that has a title.

#### Discussion

This method creates a two-line drag item preview, with the title displayed on the first line. The second line is a textual representation of the URL that might not show the full URL string. Don’t use a file URL. Passing `nil` for the title is the same as calling [`init(forURL:)`](uidragpreview/init(forurl:).md).

## Parameters

- `url`: An Internet address referencing a remote resource, such as a webpage.
- `title`: A title for the URL.

## See Also

- [convenience init(view: UIView)](uidragpreview/init(view:).md)
  Initializes a new drag item preview with a view, using the default appearance parameters.
- [init(view: UIView, parameters: UIDragPreviewParameters)](uidragpreview/init(view:parameters:).md)
  Initializes a new drag item preview with a view and with a set of appearance parameters.
- [convenience init(forURL: URL)](uidragpreview/init(forurl:).md)
  Initializes a new drag item preview with a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreview/init(forurl:title:))*