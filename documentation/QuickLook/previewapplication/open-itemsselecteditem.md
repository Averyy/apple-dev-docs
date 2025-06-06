# open(items:selectedItem:)

**Framework**: Quick Look  
**Kind**: method

Previews the provided items.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final class func open(items: [PreviewItem], selectedItem: PreviewItem? = nil) -> PreviewSession
```

#### Return Value

A `PreviewSession` instance.

#### Discussion

This method launches the preview application with the provided preview items and, optionally, a selected item.

## Parameters

- `items`: An array of preview items to present in the new   scene.
- `selectedItem`: If provided and in the array of passed items, the preview item to select in the presented collection..


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/previewapplication/open(items:selecteditem:))*