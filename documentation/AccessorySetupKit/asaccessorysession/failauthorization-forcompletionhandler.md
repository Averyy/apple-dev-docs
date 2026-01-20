# failAuthorization(for:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method

End authorization of a partially-configured accessory as a failure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func failAuthorization(for accessory: ASAccessory) async throws
```

## See Also

- [func finishAuthorization(for: ASAccessory, settings: ASAccessorySettings, completionHandler: ((any Error)?) -> Void)](asaccessorysession/finishauthorization(for:settings:completionhandler:).md)
  Finish authorization of a partially-setup accessory.
- [class ASAccessorySettings](asaccessorysettings.md)
  Properties of an accessory.
- [func updateAuthorization(for: ASAccessory, descriptor: ASDiscoveryDescriptor, completionHandler: ((any Error)?) -> Void)](asaccessorysession/updateauthorization(for:descriptor:completionhandler:).md)
  Displays a view to upgrade an accessory with additional technology permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/failauthorization(for:completionhandler:))*