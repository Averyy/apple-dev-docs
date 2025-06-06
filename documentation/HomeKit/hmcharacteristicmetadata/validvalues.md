# validValues

**Framework**: HomeKit  
**Kind**: property

The subset of valid values supported by the characteristic when the format is of type unsigned integer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var validValues: [NSNumber]? { get }
```

## See Also

- [var minimumValue: NSNumber?](hmcharacteristicmetadata/minimumvalue.md)
  The minimum value for the characteristic.
- [var maximumValue: NSNumber?](hmcharacteristicmetadata/maximumvalue.md)
  The maximum value for the characteristic.
- [var stepValue: NSNumber?](hmcharacteristicmetadata/stepvalue.md)
  The minimum interval between values for the characteristic.
- [var maxLength: NSNumber?](hmcharacteristicmetadata/maxlength.md)
  The maximum number of UTF-8 characters allowed in a characteristic that uses a string format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/validvalues)*