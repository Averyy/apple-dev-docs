# digitalCrownAccessory(_:)

**Framework**: App Intents  
**Kind**: method

Specifies the visibility of Digital Crown accessory Views on Apple Watch.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func digitalCrownAccessory(_ visibility: Visibility) -> some View
```

#### Discussion

Use this method to customize the visibility of a Digital Crown accessory `View` created with the `View/digitalCrownAccessory(_ content:)` modifier. You may want to keep an accessory visible even when the Digital Crown Indicator is not visible to indicate what scrolling the crown will do.

## Parameters

- `visibility`: The visibility of the digital crown accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/digitalcrownaccessory(_:))*