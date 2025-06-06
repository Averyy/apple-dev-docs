# isCoachingEnabled

**Framework**: RoomPlan  
**Kind**: property

An option that indicates that the session periodically provides user instructions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
var isCoachingEnabled: Bool
```

#### Discussion

When you enable this option and the framework determines the device needs a particular movement or perspective, it calls your delegate’s [`captureSession(_:didProvide:)`](roomcapturesessiondelegate/capturesession(_:didprovide:).md) and provides a particular [`RoomCaptureSession.Instruction`](roomcapturesession/instruction.md) that you can display to the user.

The default value is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/configuration/iscoachingenabled)*