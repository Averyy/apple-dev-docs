# percent()

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring percentages.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func percent() -> Self
```

#### Return Value

A HealthKit unit for measuring percentages.

#### Discussion

Percent measures a value between 0.0 and 1.0. HealthKit uses percent units when measuring body fat percentage, oxygen saturation, blood alcohol content, and similar values.  Even though count and percent units are both scalar units, you cannot convert between them.

## See Also

- [class func count() -> Self](hkunit/count.md)
  Returns a HealthKit unit for measuring counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/percent())*