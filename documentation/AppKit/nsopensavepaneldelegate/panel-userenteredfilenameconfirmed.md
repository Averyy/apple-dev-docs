# panel(_:userEnteredFilename:confirmed:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the user confirmed a filename choice by clicking Save in a Save panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, userEnteredFilename filename: String, confirmed okFlag: Bool) -> String?
```

#### Return Value

The filename selected by the user, or `nil` if you want to cancel the save operation and leave the Save panel onscreen.

#### Discussion

The Save panel calls this method before appending any required filename extension information, and before it asks the user whether to replace an existing file, if a file with the specified name already exists in the given location.

The panel may call this method multiple times as the user types. When it does, the `okFlag` parameter is [`false`](https://developer.apple.com/documentation/Swift/false). When the use confirms their choice, the value in the `okFlag` is [`true`](https://developer.apple.com/documentation/Swift/true). If your delegate does extensive validation or puts up alerts, do so only when `okFlag` is [`true`](https://developer.apple.com/documentation/Swift/true).

In macOS 10.15 and later, you cannot change the filename that the user selects. Prior to macOS 10.15, you could sanitize the app’s filename to remove undesirable characters or limit its length only if your app wasn’t running in a sandbox.

## Parameters

- `sender`: The panel that reports the user’s confirmation of a filename choice.
- `filename`: The user’s filename choice.
- `okFlag`: If  , the user clicked the Save button; if  , the user did not.

## See Also

- [func panel(Any, validate: URL) throws](nsopensavepaneldelegate/panel(_:validate:).md)
  Asks the delegate to validate the URL for a file that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:userenteredfilename:confirmed:))*