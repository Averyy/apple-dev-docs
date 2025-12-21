# NEURLFilterManager.Error

**Framework**: Network Extension  
**Kind**: enum

An enumeration of URL filter error codes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum Error
```

## Topics

### Configuration errors
- [NEURLFilterManager.Error.configurationUnchanged](neurlfiltermanager/error/configurationunchanged.md)
  The filter configuration is unchanged.
- [NEURLFilterManager.Error.configurationInvalid](neurlfiltermanager/error/configurationinvalid.md)
  The filter configuration is invalid.
- [NEURLFilterManager.Error.configurationDisabled](neurlfiltermanager/error/configurationdisabled.md)
  The filter configuration is disabled.
- [NEURLFilterManager.Error.configurationStale](neurlfiltermanager/error/configurationstale.md)
  The system needs to load the filter configuration.
- [NEURLFilterManager.Error.configurationCannotBeRemoved](neurlfiltermanager/error/configurationcannotberemoved.md)
  The system can’t remove the filter configuration.
- [NEURLFilterManager.Error.configurationPermissionDenied](neurlfiltermanager/error/configurationpermissiondenied.md)
  Operation permission denied.
- [NEURLFilterManager.Error.configurationInternalError](neurlfiltermanager/error/configurationinternalerror.md)
  An internal configuration error occurred.
- [NEURLFilterManager.Error.configurationNotLoaded](neurlfiltermanager/error/configurationnotloaded.md)
  The configuration hasn’t been loaded.
### Server errors
- [NEURLFilterManager.Error.serverSetupIncomplete](neurlfiltermanager/error/serversetupincomplete.md)
  PIR Server or/and OHTTP Private Relay setup incomplete.
### Extension errors
- [NEURLFilterManager.Error.extensionCancelled](neurlfiltermanager/error/extensioncancelled.md)
  The app extension cancelled the feature bring up.
- [NEURLFilterManager.Error.extensionNotFound](neurlfiltermanager/error/extensionnotfound.md)
  The system can’t find the app extension.
- [NEURLFilterManager.Error.extensionFailedToLoad](neurlfiltermanager/error/extensionfailedtoload.md)
  The app extension failed to load.
### Other errors
- [NEURLFilterManager.Error.internalError](neurlfiltermanager/error/internalerror.md)
  An internal error occurred.
- [NEURLFilterManager.Error.unknown](neurlfiltermanager/error/unknown.md)
  The system encountered an unknown error.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var lastDisconnectError: NEURLFilterManager.Error?](neurlfiltermanager/lastdisconnecterror.md)
  The most recent error that caused the URL Filter to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/error)*