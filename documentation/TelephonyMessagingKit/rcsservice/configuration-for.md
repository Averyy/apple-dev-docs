# configuration(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Retrieves the RCS configuration for the specified cellular service.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func configuration(for cellularServiceID: CellularServiceID) throws -> RCSService.Configuration
```

#### Discussion

You can observe changes in configuration through the [`viabilityNotifications`](rcsservice/viabilitynotifications.md) asynchronous sequence. When the service becomes viable, invoke this method to retrieve updates to the RCS configuration.

## See Also

- [RCSService.Configuration](rcsservice/configuration.md)
  A structure that contains RCS configuration parameters, such as timing and size limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration(for:))*