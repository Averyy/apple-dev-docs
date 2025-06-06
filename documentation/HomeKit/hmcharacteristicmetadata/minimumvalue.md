# minimumValue

**Framework**: HomeKit  
**Kind**: property

The minimum value for the characteristic.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var minimumValue: NSNumber? { get }
```

#### Discussion

This value only applies to characteristics with a number type.

## See Also

- [var validValues: [NSNumber]?](hmcharacteristicmetadata/validvalues.md)
  The subset of valid values supported by the characteristic when the format is of type unsigned integer.
- [var maximumValue: NSNumber?](hmcharacteristicmetadata/maximumvalue.md)
  The maximum value for the characteristic.
- [var stepValue: NSNumber?](hmcharacteristicmetadata/stepvalue.md)
  The minimum interval between values for the characteristic.
- [var maxLength: NSNumber?](hmcharacteristicmetadata/maxlength.md)
  The maximum number of UTF-8 characters allowed in a characteristic that uses a string format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/minimumvalue)*