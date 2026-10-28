# init(minValue:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates an one-sided number range with a minimum value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(minValue: NSNumber)
```

```objc
+ (instancetype) numberRangeWithMinValue:(NSNumber *) minValue;
```

## Return Value

An initialized number range, with the maximum value set to an arbitrarily large value.

## Parameters

- `minValue`: The minimum value of the range.

## See Also

### Creating a number range
- [convenience init(minValue: NSNumber, maxValue: NSNumber)](./init%28minvalue,maxvalue%29.md)
  Creates a new number range.
- [convenience init(maxValue: NSNumber)](./init%28maxvalue%29.md)
  Creates a one-sided number range with a maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnumberrange/init(minvalue:))*