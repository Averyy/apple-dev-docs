# NEFilterManagerError.configurationStale

**Framework**: Network Extension  
**Kind**: case  
**Role**: Case

An error code that indicates another process modfied the filter configuration since the last time the app loaded the configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
case configurationStale
```

```c
NEFilterManagerErrorConfigurationStale
```

#### Discussion

This error also occurs if the app tries to save the filter configuration before loading it from the Network Extension preferences the first time after the app launches.

## See Also

### Error codes
- [NEFilterManagerError.configurationInvalid](./configurationinvalid.md)
  An error code that indicates the filter configuration is invalid.
- [NEFilterManagerError.configurationDisabled](./configurationdisabled.md)
  An error code that indicates the filter configuration isn’t enabled.
- [NEFilterManagerError.configurationCannotBeRemoved](./configurationcannotberemoved.md)
  An error code that indicates removing the configuration isn’t allowed.
- [NEFilterManagerError.configurationPermissionDenied](./configurationpermissiondenied.md)
  An error code that indicates the configuration lacks permission.
- [NEFilterManagerError.configurationInternalError](./configurationinternalerror.md)
  An error code that indicates an internal configuration error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanagererror/configurationstale)*