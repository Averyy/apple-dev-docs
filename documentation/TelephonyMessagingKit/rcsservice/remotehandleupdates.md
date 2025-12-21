# remoteHandleUpdates

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of remote handle updates produced by this service.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final var remoteHandleUpdates: some AsyncSequence<RCSService.RemoteHandleUpdate, Never> { get throws }
```

#### Discussion

Use a `for`-`await`-`in` loop to receive [`RCSService.RemoteHandleUpdate`](rcsservice/remotehandleupdate.md) instances from this property.

## See Also

- [RCSService.RemoteHandleUpdate](rcsservice/remotehandleupdate.md)
  A structure that contains information about an update to a remote handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotehandleupdates)*