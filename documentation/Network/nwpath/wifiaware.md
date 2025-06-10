# wifiAware

**Framework**: Network  
**Kind**: property

Current status and performance information for Wi-Fi Aware, or `nil` if this path is not over Wi-Fi Aware.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var wifiAware: WAPath? { get async throws }
```

#### Discussion

> **Note**: An error if the path could not be retrieved, or if the App does not have access to Wi-Fi Aware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/wifiaware)*