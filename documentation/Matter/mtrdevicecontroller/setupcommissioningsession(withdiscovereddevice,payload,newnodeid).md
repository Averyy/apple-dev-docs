# setupCommissioningSession(withDiscoveredDevice:payload:newNodeID:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func setupCommissioningSession(withDiscoveredDevice discoveredDevice: MTRCommissionableBrowserResult, payload: MTRSetupPayload, newNodeID: NSNumber) throws
```

```objc
- (BOOL) setupCommissioningSessionWithDiscoveredDevice:(MTRCommissionableBrowserResult *) discoveredDevice payload:(MTRSetupPayload *) payload newNodeID:(NSNumber *) newNodeID error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/setupcommissioningsession(withdiscovereddevice:payload:newnodeid:))*