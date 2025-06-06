# count()

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring counts.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func count() -> Self
```

#### Return Value

A HealthKit unit for measuring counts.

#### Discussion

Count units are used to represent raw scalar values. They are often used to represent the number of times an event occurs—for example, the number of steps the user has taken or the number of times the user has used his or her inhaler. They can also be used as part of a compound unit—for example, the beats portion of beats per minute. Even though count and percent units are both scalar units, you cannot convert between them.

> **Note**:  In HealthKit quantities, count values are stored using `double` values, even though they are often interpreted as integers.

 In HealthKit quantities, count values are stored using `double` values, even though they are often interpreted as integers.

## See Also

- [class func percent() -> Self](hkunit/percent.md)
  Returns a HealthKit unit for measuring percentages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/count())*