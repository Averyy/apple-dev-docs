# NWPathStatus.invalid

**Framework**: Network Extension  
**Kind**: case

The path cannot be evaluated.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case invalid
```

## See Also

- [NWPathStatus.satisfied](nwpathstatus/satisfied.md)
  The path is ready to be used for network connections.
- [NWPathStatus.unsatisfied](nwpathstatus/unsatisfied.md)
  The path for network connections is not available, either due to lack of network connectivity or being prohibited by system policy.
- [NWPathStatus.satisfiable](nwpathstatus/satisfiable.md)
  The path is not currently satisfied, but may become satisfied upon a connection attempt. This can be due to a service, such as a VPN or a cellular data connection not being activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpathstatus/invalid)*