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

If an item is an [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object and contains a file URL (pointing to a video on the local disk for example), the picker shares the content of the file. If the URL is remote, then the picker shares the URL instead of the contents.

## Parameters

- `items`: The items to be shared. The items in the array must conform to the   or   protocol. For example, you can specify an  ,  ,  , or similar type directly. You can also specify   or   objects in the array to share those types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/init(items:))*