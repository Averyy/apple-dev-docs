# radius

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The App Clip Code’s radius in meters.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+

## Declaration

```swift
var radius: Float { get }
```

```objc
@property (nonatomic, assign, readonly) float radius;
```

## Discussion

ARKit estimates the value of this property at runtime. As the user views an App Clip Code from different angles, ARKit refines its estimate of the true radius of the App Clip Code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arappclipcodeanchor/radius)*