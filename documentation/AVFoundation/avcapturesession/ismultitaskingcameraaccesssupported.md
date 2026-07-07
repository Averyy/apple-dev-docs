# isMultitaskingCameraAccessSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the capture session supports using the camera while multitasking.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 17.0+

## Declaration

```swift
var isMultitaskingCameraAccessSupported: Bool { get }
```

#### Discussion

Query this property to determine whether you can use the camera while multitasking by setting the state of the [`isMultitaskingCameraAccessEnabled`](avcapturesession/ismultitaskingcameraaccessenabled.md) property to `true`.

In iOS and iPadOS, this property is `true` for any of the following cases:

- The app runs on an iPad that supports Stage Manager with an extended display.
- The app links against iOS 18 or later and uses `voip` as one of its [`UIBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes).
- The app has the [`com.apple.developer.avfoundation.multitasking-camera-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.avfoundation.multitasking-camera-access) entitlement.

In tvOS, this property is always `true`.

> **Note**:  This property is key-value observable. If the value changes from `true` to `false`, the value of [`isMultitaskingCameraAccessEnabled`](avcapturesession/ismultitaskingcameraaccessenabled.md) also changes to `false`.

To learn about best practices for using the camera while multitasking, see [`Accessing the camera while multitasking on iPad`](https://developer.apple.com/documentation/AVKit/accessing-the-camera-while-multitasking-on-ipad).

## See Also

- [var isMultitaskingCameraAccessEnabled: Bool](avcapturesession/ismultitaskingcameraaccessenabled.md)
  A Boolean value that indicates whether the capture session enables access to the camera while multitasking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccesssupported)*