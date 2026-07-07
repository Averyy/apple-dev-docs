# init(url:frame:allowedInteractions:id:)

**Framework**: PaperKit  
**Kind**: init

Initializes and returns a new link markup from the specified parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(url: URL, frame: CGRect, allowedInteractions: MarkupInteractions = .all, id: MarkupID<LinkMarkup> = MarkupID())
```

## Parameters

- `url`: The URL that the link navigates to when activated.
- `frame`: The frame of the link.
- `allowedInteractions`: The flags controlling the interactions people can perform. Defaults to `.all`.
- `id`: The identity of the link. Defaults to a unique id.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/linkmarkup/init(url:frame:allowedinteractions:id:))*