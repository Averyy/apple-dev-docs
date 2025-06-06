# GetWorkQueue

**Framework**: AudioDriverKit  
**Kind**: method

Gets the work queue created by the audio object, as a pointer to a dispatch queue.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
OSSharedPtr<IODispatchQueue> GetWorkQueue();
```

#### Return Value

The work queue created by the audio object.

#### Discussion

The work queue synchronizes access to the driver’s state. Setters and getters for the driver do their work on the work queue.

## See Also

- [GetClassID](iouseraudiodriver/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiodriver/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetName](iouseraudiodriver/getname.md)
  Gets the name of the driver.
- [SetName](iouseraudiodriver/setname.md)
  Sets the name of the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/getworkqueue)*