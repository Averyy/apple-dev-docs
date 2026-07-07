# maximumDepth

**Framework**: Core Motion  
**Kind**: property

The maximum depth supported by the water submersion manager.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var maximumDepth: Measurement<UnitLength>? { get }
```

#### Discussion

To access data for dives with a maximum depth of 6 m, add the Shallow Depth and Pressure capability to your app. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

To enable a maximum depth of 40 m, you must apply for the full Submerged Depth and Pressure entitlement. For more information, see [`Express interest in the Submerged Depth and Pressure API`](https://developer.apple.comhttps://developer.apple.com/contact/request/submerged-depth-pressure-api/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager/maximumdepth)*