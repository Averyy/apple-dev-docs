# deviceFitStatus

**Framework**: ARKit  
**Kind**: property

The device fit validation status.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var deviceFitStatus: DeviceFitStatus { get }
```

#### Discussion

Indicates whether the user’s eyes are properly positioned within the optimal device fit range, or provides directional feedback if positioned outside.

Note: Returns `.unknown` if the provider was created without requesting device fit updates, or when the status cannot be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/visualfidelitydata/devicefitstatus)*