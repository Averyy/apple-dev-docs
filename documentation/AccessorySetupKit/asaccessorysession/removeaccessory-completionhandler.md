# removeAccessory(_:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method

Removes an accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func removeAccessory(_ accessory: ASAccessory) async throws
```

## Parameters

- `accessory`: The accessory to remove.
- `completionHandler`: A block or closure that executes after the remove operation completes. The completion handler receives an   instance if the remove operation encounters an error.

## See Also

- [func renameAccessory(ASAccessory, options: ASAccessory.RenameOptions, completionHandler: ((any Error)?) -> Void)](asaccessorysession/renameaccessory(_:options:completionhandler:).md)
  Displays a view to rename an accessory.
- [ASAccessory.RenameOptions](asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/removeaccessory(_:completionhandler:))*