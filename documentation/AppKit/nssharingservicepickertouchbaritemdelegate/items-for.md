# items(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks the delegate for items that represent the objects to be shared.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func items(for pickerTouchBarItem: NSSharingServicePickerTouchBarItem) -> [Any]
```

#### Return Value

An array of items that represents the objects to be shared. Each element of the array must either conform to the [`NSPasteboardWriting`](nspasteboardwriting.md) protocol, or be an [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider).

## Parameters

- `pickerTouchBarItem`: The sharing service picker item that is requesting the items to be shared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritemdelegate/items(for:))*