# stopMonitoringLocationPushes()

**Framework**: Core Location  
**Kind**: method

Stops monitoring for Apple Push Notification service (APNs) location pushes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
func stopMonitoringLocationPushes()
```

#### Discussion

Call this method to stop the device from monitoring for APNs location pushes. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

## See Also

- [func startMonitoringLocationPushes(completion: ((Data?, (any Error)?) -> Void)?)](cllocationmanager/startmonitoringlocationpushes(completion:).md)
  Starts monitoring for the delivery of Apple Push Notification service (APNs) location pushes, and provides a device-specific token for sending pushes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/stopmonitoringlocationpushes())*