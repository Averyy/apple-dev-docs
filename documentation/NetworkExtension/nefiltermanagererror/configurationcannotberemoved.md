# NEFilterManagerError.configurationCannotBeRemoved

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

An error code that indicates removing the configuration isn’t allowed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
case configurationCannotBeRemoved
```

```c
NEFilterManagerErrorConfigurationCannotBeRemoved
```

## See Also

### Error codes
- [NEFilterManagerError.configurationInvalid](./configurationinvalid.md)
  An error code that indicates the filter configuration is invalid.
- [NEFilterManagerError.configurationDisabled](./configurationdisabled.md)
  An error code that indicates the filter configuration isn’t enabled.
- [NEFilterManagerError.configurationStale](./configurationstale.md)
  An error code that indicates another process modfied the filter configuration since the last time the app loaded the configuration.
- [NEFilterManagerError.configurationPermissionDenied](./configurationpermissiondenied.md)
  An error code that indicates the configuration lacks permission.
- [NEFilterManagerError.configurationInternalError](./configurationinternalerror.md)
  An error code that indicates an internal configuration error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationcannotberemoved)*