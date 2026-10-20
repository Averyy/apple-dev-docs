# frictionSlip

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The traction between the wheel and any surface in contact with it.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var frictionSlip: CGFloat { get set }
```

```objc
@property CGFloat frictionSlip;
```

#### Discussion

The default value of this property is `1.0`. Lower values result in better traction, and higher values make the wheel more likely to slip (causing it to spin freely instead of moving the vehicle).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/frictionslip)*