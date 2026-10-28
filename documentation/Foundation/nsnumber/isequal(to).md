# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the number object’s value and a given number are equal.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isEqual(to number: NSNumber) -> Bool
```

```objc
- (BOOL) isEqualToNumber:(NSNumber *) number;
```

## Return Value

[`true`](../../Swift/true.md) if the number object’s value and `number` are equal, otherwise [`false`](../../Swift/false.md).

## Discussion

Two `NSNumber` objects are considered equal if they have the same id values or if they have equivalent values (as determined by the [`compare(_:)`](./compare%28_%29.md) method).

This method is more efficient than [`compare(_:)`](./compare%28_%29.md) if you know the two objects are numbers.

## Parameters

- `number`: The number to compare to the number object’s value.

## See Also

### Comparing NSNumber Objects
- [func compare(NSNumber) -> ComparisonResult](./compare%28_%29.md)
  Returns an `NSComparisonResult` value that indicates whether the number object’s value is greater than, equal to, or less than a given number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnumber/isequal(to:))*