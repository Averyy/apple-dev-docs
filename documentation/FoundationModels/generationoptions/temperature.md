# temperature

**Framework**: Foundation Models  
**Kind**: property

Temperature influences the confidence of the models response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var temperature: Double?
```

#### Discussion

The value of this property must be a number between `0` and `2` inclusive.

Temperature is an adjustment applied  to the probability distribution prior to sampling. A value of `1` results in no adjustment. Values less than `1` will make the probability distribution sharper, with already likely tokens becoming even more likely. Values greather than `1` will flatten the distribution, making less probable tokens more likely.

The net effect is that low temperatures manifest as more stable and predictable responses, while high temperatures give the model more creative license.

> **Note**: Leaving `temperature` nil lets the system choose a reasonable default on your behalf.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/temperature)*