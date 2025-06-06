# SetName

**Framework**: AudioDriverKit  
**Kind**: method

Sets the name of the object.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetName(OSString * in_name);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If the change succeeds, the framework sends a notification to the host to update its object state. Setting the name synchronizes by using the work queue created by the object.

## Parameters

- `in_name`: The name to set, as an  .

## See Also

- [GetName](iouseraudioobject/getname.md)
  Gets the name of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/setname)*