# init(ecoScore:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for an eco-score rating.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(ecoScore value: Double)
```

#### Return Value

A new @c CPRouteDetail instance representing the eco-score

#### Discussion

Use this method to display a normalized environmental efficiency score for the route. The score should be a value between 0.0 and 100.0, where higher values indicate more environmentally friendly routing options.

The eco-score can incorporate multiple factors including carbon emissions, fuel efficiency, traffic congestion impact, terrain characteristics, and route optimization. The system displays this as a percentage-like value with appropriate visual indicators. Use consistent calculation methodology across all routes to enable meaningful comparison.

> **Note**: The interpretation and calculation methodology of eco-scores may vary by app. Consider documenting your scoring algorithm in your app’s help or settings, and ensure the score remains consistent across app updates to maintain user trust and understanding.

## Parameters

- `value`: The eco-score rating from 0.0 to 100.0. Values outside this range will be clamped. Higher scores indicate more environmentally friendly routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(ecoscore:))*