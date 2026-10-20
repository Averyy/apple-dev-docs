# removeAccessory(_:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method  
**Role**: Instance Method

Removes an accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func removeAccessory(_ accessory: ASAccessory, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeAccessory(_ accessory: ASAccessory) async throws
```

```objc
- (void) removeAccessory:(ASAccessory *) accessory completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `accessory`: The accessory to remove.
- `completionHandler`: A block or closure that executes after the remove operation completes. The completion handler receives an [`NSError`](../../Foundation/nserror.md) instance if the remove operation encounters an error.

## See Also

### Managing accessories
- [func renameAccessory(ASAccessory, options: ASAccessory.RenameOptions, completionHandler: ((any Error)?) -> Void)](./renameaccessory%28_,options,completionhandler%29.md)
  Displays a view to rename an accessory.
- [ASAccessory.RenameOptions](../asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/removeaccessory(_:completionhandler:))*