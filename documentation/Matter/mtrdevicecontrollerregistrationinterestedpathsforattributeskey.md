# MTRDeviceControllerRegistrationInterestedPathsForAttributesKey

**Framework**: Matter  
**Kind**: var  
**Role**: Global Variable

A node entry carries the union of its delegates’ interested paths, sorted, under MTRDeviceControllerRegistrationInterestedPathsForAttributesKey and MTRDeviceControllerRegistrationInterestedPathsForEventsKey. The attribute paths include those of pending attribute-value waiters, so a node with only waiters is listed too. A missing key means every path. Each element is an NSNumber endpoint ID, or a dictionary of NSNumbers holding MTRDeviceControllerRegistrationInterestedPathEndpointIDKey and MTRDeviceControllerRegistrationInterestedPathClusterIDKey, plus MTRDeviceControllerRegistrationInterestedPathAttributeIDKey for an attribute path or MTRDeviceControllerRegistrationInterestedPathEventIDKey for an event path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let MTRDeviceControllerRegistrationInterestedPathsForAttributesKey: String
```

```c
extern NSString * const MTRDeviceControllerRegistrationInterestedPathsForAttributesKey;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationinterestedpathsforattributeskey)*