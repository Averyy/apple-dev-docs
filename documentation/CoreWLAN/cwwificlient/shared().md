# shared()

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Type Method

The shared Wi-Fi client object.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func shared() -> CWWiFiClient
```

```objc
+ (CWWiFiClient *) sharedWiFiClient;
```

## Discussion

Each process spawns its own shared instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/shared())*