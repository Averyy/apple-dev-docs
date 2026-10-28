# preventsExpensiveNetworkAccess

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Prevents expensive network access, such as cellular, for the service.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var preventsExpensiveNetworkAccess: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL preventsExpensiveNetworkAccess;
```

## Discussion

When `true`, the service only performs work for the associated configuration while the device has a non-expensive network connection (such as Wi-Fi or Ethernet); cellular connectivity is not used. Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourceuploadjoboptions/preventsexpensivenetworkaccess)*