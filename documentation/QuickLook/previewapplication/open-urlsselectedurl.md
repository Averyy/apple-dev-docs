# open(urls:selectedURL:)

**Framework**: Quick Look  
**Kind**: method

Previews the provided URLs.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final class func open(urls: [URL], selectedURL: URL? = nil) -> PreviewSession
```

#### Return Value

A `PreviewSession` instance.

#### Discussion

This method launches the preview application with the provided URLs and, optionally, a selected URL.

## Parameters

- `urls`: An array of URLs to present in the new   scene.
- `selectedURL`: If provided and in the array of passed URLs, the URL to select in the presented collection..


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/previewapplication/open(urls:selectedurl:))*