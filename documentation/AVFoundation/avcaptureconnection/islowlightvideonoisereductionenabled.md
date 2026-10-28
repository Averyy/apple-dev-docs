# isLowLightVideoNoiseReductionEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether low light video noise reduction is enabled for the current session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var isLowLightVideoNoiseReductionEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isLowLightVideoNoiseReductionEnabled) BOOL lowLightVideoNoiseReductionEnabled;
```

## Discussion

A `BOOL` indicating whether low light video noise reduction is enabled on the connection. To set this property directly, first set [`automaticallyEnablesLowLightVideoNoiseReduction`](./automaticallyenableslowlightvideonoisereduction.md) to `false`; setting this property while [`automaticallyEnablesLowLightVideoNoiseReduction`](./automaticallyenableslowlightvideonoisereduction.md) is `true` throws an `NSInvalidArgumentException`. This property may only be set to `true` if the connection’s [`isLowLightVideoNoiseReductionSupported`](./islowlightvideonoisereductionsupported.md) property returns `true`, otherwise an `NSInvalidArgumentException` is thrown. This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/islowlightvideonoisereductionenabled)*