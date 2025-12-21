# setDataProvider(_:forTypes:)

**Framework**: AppKit  
**Kind**: method

Sets the data provider for the specified types.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setDataProvider(_ dataProvider: any NSPasteboardItemDataProvider, forTypes types: [NSPasteboard.PasteboardType]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the data provider was set successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method registers the data provider to be messaged to provide the data for any of the specified types when requested.

## Parameters

- `dataProvider`: A pasteboard data provider.
- `types`: An array of strings indicating the UTIs for the data representations   may provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/setdataprovider(_:fortypes:))*