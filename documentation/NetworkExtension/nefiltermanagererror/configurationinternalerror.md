# NEFilterManagerError.configurationInternalError

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

An error code that indicates an internal configuration error occurred.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case configurationInternalError
```

```c
NEFilterManagerErrorConfigurationInternalError
```

## See Also

### Error codes
- [NEFilterManagerError.configurationInvalid](./configurationinvalid.md)
  An error code that indicates the filter configuration is invalid.
- [NEFilterManagerError.configurationDisabled](./configurationdisabled.md)
  An error code that indicates the filter configuration isn’t enabled.
- [NEFilterManagerError.configurationStale](./configurationstale.md)
  An error code that indicates another process modfied the filter configuration since the last time the app loaded the configuration.
- [NEFilterManagerError.configurationCannotBeRemoved](./configurationcannotberemoved.md)
  An error code that indicates removing the configuration isn’t allowed.
- [NEFilterManagerError.configurationPermissionDenied](./configurationpermissiondenied.md)
  An error code that indicates the configuration lacks permission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationinternalerror)*