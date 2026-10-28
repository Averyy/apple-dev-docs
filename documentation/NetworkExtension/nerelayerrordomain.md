# NERelayErrorDomain

**Framework**: Network Extension  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const NERelayErrorDomain;
```

## Discussion

Match this constant to the [`domain`](../Foundation/nserror/domain.md) of an [`NSError`](../Foundation/nserror.md) encountered when calling methods on [`NERelayManager`](./nerelaymanager.md). The [`NERelayManagerError`](./nerelaymanagererror.md) enumeration defines possible [`code`](../Foundation/nserror/code.md) values for these errors.

## See Also

### Handling errors
- [enum NERelayManagerError](./nerelaymanagererror.md)
  Error codes specific to relay managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelayerrordomain)*