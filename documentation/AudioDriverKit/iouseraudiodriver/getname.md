# GetName

**Framework**: AudioDriverKit  
**Kind**: method

Gets the name of the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
OSSharedPtr<OSString> GetName();
```

#### Return Value

A `OSSharedPtr` to an [`OSString`](https://developer.apple.com/documentation/DriverKit/OSString) containing the driver name.

#### Discussion

Getting the name synchronizes by using the work queue created by the object.

## See Also

- [GetClassID](iouseraudiodriver/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiodriver/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetWorkQueue](iouseraudiodriver/getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.
- [SetName](iouseraudiodriver/setname.md)
  Sets the name of the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/getname)*