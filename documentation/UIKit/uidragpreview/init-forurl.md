# init(forURL:)

**Framework**: UIKit  
**Kind**: init

Initializes a new drag item preview with a URL.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
convenience init(for url: URL)
```

#### Return Value

A drag preview for a URL.

#### Discussion

This method creates a drag item preview of the URL. The URL preview is a one-line, textual representation that might not show the full URL string. Don’t use a file URL.

## Parameters

- `url`: An Internet address referencing a remote resource, such as a webpage.

## See Also

- [convenience init(view: UIView)](uidragpreview/init(view:).md)
  Initializes a new drag item preview with a view, using the default appearance parameters.
- [init(view: UIView, parameters: UIDragPreviewParameters)](uidragpreview/init(view:parameters:).md)
  Initializes a new drag item preview with a view and with a set of appearance parameters.
- [convenience init(forURL: URL, title: String?)](uidragpreview/init(forurl:title:).md)
  Initializes a drag item preview with a URL and title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreview/init(forurl:))*