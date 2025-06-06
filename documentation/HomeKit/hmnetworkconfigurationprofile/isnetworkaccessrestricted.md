# isNetworkAccessRestricted

**Framework**: HomeKit  
**Kind**: property

An indication of whether the accessory’s access to the network is restricted.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isNetworkAccessRestricted: Bool { get }
```

#### Discussion

When the value is `true`, the accessory experiences restricted network access. When the value is `false`, the accessory’s access to the network isn’t restricted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnetworkconfigurationprofile/isnetworkaccessrestricted)*