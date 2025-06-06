# HandleChangeCustomPropertyDataValueWithQualifier

**Framework**: AudioDriverKit  
**Kind**: method

Tells the property the data value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeCustomPropertyDataValueWithQualifier(OSObject * in_qualifier_data, OSObject * in_data);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation sets the value and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess), without checking the qualifier data. Subclass and override this method to handle changes to the custom property and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) upon success.

## Parameters

- `in_qualifier_data`: The qualifier data   associated with setting the property data value. This can be an  ,  , or  .
- `in_data`: An   to set as the custom property value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/handlechangecustompropertydatavaluewithqualifier)*