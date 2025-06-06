# items(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks the delegate for the items to share.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
func items(for pickerToolbarItem: NSSharingServicePickerToolbarItem) -> [Any]
```

#### Return Value

An array of items to share using the share sheet.

#### Discussion

In your implementation of this method, return the items in the current window that you want to share. Return the content that is focal to your window or is currently selected. For example, you might share the current photo someone is viewing. For a document window, you might share the document itself.

## Parameters

- `pickerToolbarItem`: The toolbar item that displays the share sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertoolbaritemdelegate/items(for:))*