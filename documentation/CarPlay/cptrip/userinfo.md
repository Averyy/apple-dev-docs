# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A custom object associated with the trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var userInfo: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id userInfo;
```

#### Discussion

Use this property to store any arbitrary data related to the trip that you may need at a later date, or by another part of your app that consumes trips.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrip/userinfo)*