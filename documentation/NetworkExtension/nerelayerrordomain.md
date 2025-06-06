# NERelayErrorDomain

**Framework**: Network Extension  
**Kind**: var

The domain for errors resulting from calls to the relay manager.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
let NERelayErrorDomain: String
```

#### Discussion

Match this constant to the [`domain`](https://developer.apple.com/documentation/foundation/nserror/1413924-domain) of an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) encountered when calling methods on [`NERelayManager`](nerelaymanager.md). The [`NERelayManagerError`](nerelaymanagererror.md) enumeration defines possible [`code`](https://developer.apple.com/documentation/foundation/nserror/1409165-code) values for these errors.

## See Also

- [enum NERelayManagerError](nerelaymanagererror.md)
  Error codes specific to relay managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelayerrordomain)*