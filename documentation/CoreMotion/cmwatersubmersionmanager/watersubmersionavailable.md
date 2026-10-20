# waterSubmersionAvailable

**Framework**: Core Motion  
**Kind**: property  
**Role**: Type Property

A Boolean value indicating whether the current device supports the submersion manager.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class var waterSubmersionAvailable: Bool { get }
```

```objc
@property (class, nonatomic, readonly) BOOL waterSubmersionAvailable;
```

## Mentions

- [Accessing submersion data](../accessing-submersion-data.md)

#### Discussion

On Apple Watch Ultra, the system sets `waterSubmersionAvailable` to [`true`](../../Swift/true.md). On all other devices and in Simulator, the system sets it to [`false`](../../Swift/false.md).

## See Also

### Checking availability and authorization
- [class var authorizationStatus: CMAuthorizationStatus](./authorizationstatus.md)
  A value indicating whether the app has user authorization to receive submersion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/watersubmersionavailable)*