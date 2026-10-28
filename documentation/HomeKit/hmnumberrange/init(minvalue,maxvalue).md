# init(minValue:maxValue:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a new number range.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(minValue: NSNumber, maxValue: NSNumber)
```

```objc
+ (instancetype) numberRangeWithMinValue:(NSNumber *) minValue maxValue:(NSNumber *) maxValue;
```

## Return Value

An initialized number range.

## Parameters

- `minValue`: The minimum value of the range.
- `maxValue`: The maximum value of the range.

## See Also

### Creating a number range
- [convenience init(minValue: NSNumber)](./init%28minvalue%29.md)
  Creates an one-sided number range with a minimum value.
- [convenience init(maxValue: NSNumber)](./init%28maxvalue%29.md)
  Creates a one-sided number range with a maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnumberrange/init(minvalue:maxvalue:))*