# init(items:)

**Framework**: AppKit  
**Kind**: init

Creates a new sharing service picker for the selected items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(items: [Any])
```

#### Return Value

A configured sharing service picker.

#### Discussion

If an item is an [`NSURL`](https://developer.apple.com/documentation/foundation/nsurl) object and contains a file URL (pointing to a video on the local disk for example), the picker shares the content of the file. If the URL is remote, then the picker shares the URL instead of the contents.

## Parameters

- `items`: The items to be shared. The items in the array must conform to the [`NSPasteboardWriting`](nspasteboardwriting.md) or [`NSPreviewRepresentableActivityItem`](nspreviewrepresentableactivityitem.md) protocol. For example, you can specify an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring), [`NSImage`](nsimage.md), [`NSURL`](https://developer.apple.com/documentation/foundation/nsurl), or similar type directly. You can also specify [`NSItemProvider`](https://developer.apple.com/documentation/foundation/nsitemprovider) or [`NSDocument`](nsdocument.md) objects in the array to share those types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/init(items:))*