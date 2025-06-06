# performAction(identifier:onItemsWithIdentifiers:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the File Provider extension to perform a custom action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func performAction(identifier actionIdentifier: NSFileProviderExtensionActionIdentifier, onItemsWithIdentifiers itemIdentifiers: [NSFileProviderItemIdentifier], completionHandler: @escaping ((any Error)?) -> Void) -> Progress
```

#### Return Value

An item that tracks your extension’s progress.

#### Discussion

Define the custom actions in the File Provider Extension’s `Info.plist` file, under the `NSExtensionFileProviderActions` key. The format of this key is identical to actions defined for a [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) extension. For more information, see `Adding Actions to the Context Menu`.

## Parameters

- `actionIdentifier`: The identifier for the requested custom action from the extension’s   file.
- `itemIdentifiers`: A list of item identifiers affected by the action.
- `completionHandler`: A block that you call after completing the specified action. You pass the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercustomaction/performaction(identifier:onitemswithidentifiers:completionhandler:))*