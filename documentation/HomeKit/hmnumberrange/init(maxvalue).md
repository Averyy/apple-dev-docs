# init(maxValue:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a one-sided number range with a maximum value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(maxValue: NSNumber)
```

```objc
+ (instancetype) numberRangeWithMaxValue:(NSNumber *) maxValue;
```

## Return Value

An initialized number range, with the minimum value set to an arbitrarily large negative value.

## Parameters

- `maxValue`: The maximum value of the range.

## See Also

### Creating a number range
- [convenience init(minValue: NSNumber, maxValue: NSNumber)](./init%28minvalue,maxvalue%29.md)
  Creates a new number range.
- [convenience init(minValue: NSNumber)](./init%28minvalue%29.md)
  Creates an one-sided number range with a minimum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnumberrange/init(maxvalue:))*