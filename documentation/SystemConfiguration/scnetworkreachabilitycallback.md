# SCNetworkReachabilityCallBack

**Framework**: System Configuration  
**Kind**: typealias

Type of callback function used when the reachability of a network address or name changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias SCNetworkReachabilityCallBack = (SCNetworkReachability, SCNetworkReachabilityFlags, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `target`: The network target being monitored for changes.
- `flags`: The flags representing the reachability status of the network address or name (see   for information about these flags).
- `info`: A C pointer to a user-specified block of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycallback)*