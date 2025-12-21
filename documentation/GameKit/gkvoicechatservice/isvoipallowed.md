# isVoIPAllowed()

**Framework**: GameKit  
**Kind**: method

Returns whether voice chat is allowed to be used on the device.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func isVoIPAllowed() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if voice chat is available to the application.

#### Discussion

Some countries or phone carriers may restrict the availability of voice over IP services. Before retrieving the shared voice chat service object, your application should check to see whether voice chat is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/isvoipallowed())*