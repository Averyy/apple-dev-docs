# GetName

**Framework**: AudioDriverKit  
**Kind**: method

Gets the name of the object.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
OSSharedPtr<OSString> GetName();
```

#### Return Value

A `OSSharedPtr` to an [`OSString`](https://developer.apple.com/documentation/DriverKit/OSString) containing the object name.

#### Discussion

Getting the name synchronizes by using the work queue created by the object.

## See Also

- [SetName](iouseraudioobject/setname.md)
  Sets the name of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/getname)*