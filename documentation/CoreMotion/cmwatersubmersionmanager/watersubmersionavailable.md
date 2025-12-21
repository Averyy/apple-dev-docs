# waterSubmersionAvailable

**Framework**: Core Motion  
**Kind**: property

A Boolean value indicating whether the current device supports the submersion manager.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class var waterSubmersionAvailable: Bool { get }
```

## Mentions

- [Accessing submersion data](accessing-submersion-data.md)

#### Discussion

On Apple Watch Ultra, the system sets `waterSubmersionAvailable` to [`true`](https://developer.apple.com/documentation/Swift/true). On all other devices and in Simulator, the system sets it to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [class var authorizationStatus: CMAuthorizationStatus](cmwatersubmersionmanager/authorizationstatus.md)
  A value indicating whether the app has user authorization to receive submersion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/watersubmersionavailable)*