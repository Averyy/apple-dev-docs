# configuration(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Retrieves the MMS configuration for the carrier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func configuration(for cellularServiceID: CellularServiceID) async throws -> MMSService.Configuration
```

#### Return Value

An [`MMSService.Configuration`](mmsservice/configuration.md) instance that describes the MMS configuration.

#### Discussion

Fetch the MMS configuration when your app launches and during susbscription change events.

> **Note**: - [`TelephonyMessagingSession.Error.invalidSession`](telephonymessagingsession/error/invalidsession.md) if the session isn’t valid.

## Parameters

- `cellularServiceID`: The cellular service identifier for which to fetch the MMS configuration.

## See Also

- [MMSService.Configuration](mmsservice/configuration.md)
  A structure that provides information about MMS messages sent and received using the current carrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/configuration(for:))*