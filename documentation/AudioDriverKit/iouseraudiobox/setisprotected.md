# SetIsProtected

**Framework**: AudioDriverKit  
**Kind**: method

Sets a Boolean value that indicates if the box requires authentication before use.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetIsProtected(bool in_is_protected);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the protection state sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_is_protected`: The new value of the box’s protection state.

## See Also

- [IsProtected](iouseraudiobox/isprotected.md)
  Returns a Boolean value that indicates if the box requires authentication before use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/setisprotected)*