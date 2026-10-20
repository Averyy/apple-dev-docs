# HandleChangeCustomPropertyDataValueWithQualifier

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the property the data value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeCustomPropertyDataValueWithQualifier(OSObject *in_qualifier_data, OSObject *in_data);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The default implementation sets the value and returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md), without checking the qualifier data. Subclass and override this method to handle changes to the custom property and return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) upon success.

## Parameters

- `in_qualifier_data`: The qualifier data [`OSObject`](../../DriverKit/osobject.md) associated with setting the property data value. This can be an [`OSString`](../../DriverKit/osstring.md), [`OSDictionary`](../../DriverKit/osdictionary.md), or `NULL`.
- `in_data`: An [`OSObject`](../../DriverKit/osobject.md) to set as the custom property value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/handlechangecustompropertydatavaluewithqualifier)*