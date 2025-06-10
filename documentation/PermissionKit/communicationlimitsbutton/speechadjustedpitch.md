# speechAdjustedPitch(_:)

**Framework**: PermissionKit  
**Kind**: method

Raises or lowers the pitch of spoken text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 8.0+

## Declaration

```swift
nonisolated
func speechAdjustedPitch(_ value: Double) -> some View
```

#### Discussion

Use this modifier when you want to change the pitch of spoken text. The value indicates how much higher or lower to change the pitch.

## Parameters

- `value`: The amount to raise or lower the pitch.   Values between   and   result in a lower pitch while   values between   and   result in a higher pitch.   The method clamps values to the range   to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/speechadjustedpitch(_:))*