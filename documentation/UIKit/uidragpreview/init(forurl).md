# init(forURL:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a new drag item preview with a URL.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
convenience init(forURL url: URL)
```

#### Return Value

A drag preview for a URL.

#### Discussion

This method creates a drag item preview of the URL. The URL preview is a one-line, textual representation that might not show the full URL string. Don’t use a file URL.

## Parameters

- `url`: An Internet address referencing a remote resource, such as a webpage.

## See Also

### Initializing a drag item preview
- [convenience init(view: UIView)](./init%28view%29.md)
  Initializes a new drag item preview with a view, using the default appearance parameters.
- [init(view: UIView, parameters: UIDragPreviewParameters)](./init%28view,parameters%29.md)
  Initializes a new drag item preview with a view and with a set of appearance parameters.
- [convenience init(forURL: URL, title: String?)](./init%28forurl,title%29.md)
  Initializes a drag item preview with a URL and title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragpreview/init(forurl:))*