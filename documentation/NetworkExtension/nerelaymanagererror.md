# NERelayManagerError

**Framework**: Network Extension  
**Kind**: enum

Error codes specific to relay managers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NERelayManagerError
```

## Topics

### Error codes
- [NERelayManagerError.configurationInvalid](nerelaymanagererror/configurationinvalid.md)
  An error code that indicates the relay manager is invalid.
- [NERelayManagerError.configurationDisabled](nerelaymanagererror/configurationdisabled.md)
  An error code that indicates the relay manager isn’t enabled.
- [NERelayManagerError.configurationStale](nerelaymanagererror/configurationstale.md)
  An error code that indicates the relay manager isn’t loaded.
- [NERelayManagerError.configurationCannotBeRemoved](nerelaymanagererror/configurationcannotberemoved.md)
  An error code that indicates removing the relay manager failed.
### Initializers
- [init?(rawValue: Int)](nerelaymanagererror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let NERelayErrorDomain: String](nerelayerrordomain.md)
  The domain for errors resulting from calls to the relay manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanagererror)*