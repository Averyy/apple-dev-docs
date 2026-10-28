# SetIsProtected

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value that indicates if the box requires authentication before use.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetIsProtected(bool in_is_protected);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

If successful, changing the protection state sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_is_protected`: The new value of the box’s protection state.

## See Also

### Managing Protection State
- [IsProtected](./isprotected.md)
  Returns a Boolean value that indicates if the box requires authentication before use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/setisprotected)*