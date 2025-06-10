# NEFilterManagerError

**Framework**: Network Extension  
**Kind**: enum

Error codes specific to filter managers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
enum NEFilterManagerError
```

## Topics

### Error codes
- [NEFilterManagerError.configurationInvalid](nefiltermanagererror/configurationinvalid.md)
  An error code that indicates the filter configuration is invalid.
- [NEFilterManagerError.configurationDisabled](nefiltermanagererror/configurationdisabled.md)
  An error code that indicates the filter configuration isn’t enabled.
- [NEFilterManagerError.configurationStale](nefiltermanagererror/configurationstale.md)
  An error code that indicates another process modfied the filter configuration since the last time the app loaded the configuration.
- [NEFilterManagerError.configurationCannotBeRemoved](nefiltermanagererror/configurationcannotberemoved.md)
  An error code that indicates removing the configuration isn’t allowed.
- [NEFilterManagerError.configurationPermissionDenied](nefiltermanagererror/configurationpermissiondenied.md)
  An error code that indicates the configuration lacks permission.
- [NEFilterManagerError.configurationInternalError](nefiltermanagererror/configurationinternalerror.md)
  An error code that indicates an internal configuration error occurred.
### Initializers
- [init?(rawValue: Int)](nefiltermanagererror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let NEFilterErrorDomain: String](nefiltererrordomain.md)
  The domain for errors resulting from calls to the filter manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanagererror)*