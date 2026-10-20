# SCNetworkReachabilityGetFlags(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Determines if the specified network target is reachable using the current network configuration.

**Availability**:
- iOS 2.0+ - Deprecated in 17.4
- iPadOS 2.0+ - Deprecated in 17.4
- Mac Catalyst 13.1+ - Deprecated in 17.4
- macOS 10.3+ - Deprecated in 14.4
- tvOS - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

## Declaration

```swift
func SCNetworkReachabilityGetFlags(_ target: SCNetworkReachability, _ flags: UnsafeMutablePointer<SCNetworkReachabilityFlags>) -> Bool
```

```c
Boolean SCNetworkReachabilityGetFlags(SCNetworkReachabilityRef target, SCNetworkReachabilityFlags *flags);
```

#### Return Value

`TRUE` if the flags are valid; `FALSE` if the status could not be determined.

## Parameters

- `target`: The network reference associated with the address or name to be checked for reachability.
- `flags`: A pointer to memory that, on output, is filled with flags that describe the reachability of the specified target. (See [`SCNetworkReachabilityFlags`](./scnetworkreachabilityflags.md) for possible values.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitygetflags(_:_:))*