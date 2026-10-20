# GetName

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the name of the object.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
OSSharedPtr<OSString> GetName();
```

#### Return Value

A `OSSharedPtr` to an [`OSString`](../../DriverKit/osstring.md) containing the object name.

#### Discussion

Getting the name synchronizes by using the work queue created by the object.

## See Also

### Working with Object Names
- [SetName](./setname.md)
  Sets the name of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/getname)*