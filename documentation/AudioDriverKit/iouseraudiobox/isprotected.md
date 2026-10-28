# IsProtected

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the box requires authentication before use.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
bool IsProtected();
```

## Return Value

`true` if the box is protected; `false` otherwise.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Managing Protection State
- [SetIsProtected](./setisprotected.md)
  Sets a Boolean value that indicates if the box requires authentication before use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/isprotected)*