# accessibilityAllowedValues

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The allowed values for the slider accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```objc
@property (copy, nullable) NSArray<NSNumber *> * accessibilityAllowedValues;
```

## Discussion

Use this property if the slider can be set only to predefined values (for example, if the slider’s level indicator automatically snaps to the closest integer values between 0 and 100).

## See Also

### Configuring sliders
- [accessibilityLabelUIElements](./accessibilitylabeluielements.md)
  The child label elements for the slider accessibility element.
- [accessibilityLabelValue](./accessibilitylabelvalue.md)
  The value of the label accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilityallowedvalues)*