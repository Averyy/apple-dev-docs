# SetName

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the name of the object.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetName(OSString *in_name);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

If the change succeeds, the framework sends a notification to the host to update its object state. Setting the name synchronizes by using the work queue created by the object.

## Parameters

- `in_name`: The name to set, as an [`OSString`](../../DriverKit/osstring.md).

## See Also

### Working with Object Names
- [GetName](./getname.md)
  Gets the name of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/setname)*