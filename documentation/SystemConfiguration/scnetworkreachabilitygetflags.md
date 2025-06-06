# SCNetworkReachabilityGetFlags(_:_:)

**Framework**: System Configuration  
**Kind**: func

Determines if the specified network target is reachable using the current network configuration.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCNetworkReachabilityGetFlags(_ target: SCNetworkReachability, _ flags: UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Bool
```

#### Return Value

`TRUE` if the flags are valid; `FALSE` if the status could not be determined.

## Parameters

- `target`: The network reference associated with the address or name to be checked for reachability.
- `flags`: A pointer to memory that, on output, is filled with flags that describe the reachability of the specified target. (See   for possible values.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitygetflags(_:_:))*