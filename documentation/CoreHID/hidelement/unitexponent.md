# unitExponent

**Framework**: Core HID  
**Kind**: property

The calculated exponent for this element.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var unitExponent: Int8?
```

#### Discussion

Some items in the report descriptor have exponent codes associated with them. The code specifies the exponent that should be applied to the scaled and shifted logical value to calculate the physical value. The value here represents the actual exponent value, calculated from the code specified in the report descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/unitexponent)*