# Create

**Framework**: AudioDriverKit  
**Kind**: method

Allocates and initializes an instance of the audio box class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
static OSSharedPtr<IOUserAudioBox> Create(IOUserAudioDriver * in_driver, bool in_is_acquirable, OSString * in_box_uid);
```

#### Return Value

A poiner to an [`IOUserAudioBox`](iouseraudiobox.md), if allocation and initialization succeeded.

#### Discussion

If you subclass [`IOUserAudioBox`](iouseraudiobox.md) to override this class’ behavior, don’t use [`Create`](iouseraudiobox/create.md) to allocate and initialize the custom subclass.

## Parameters

- `in_driver`: The   that owns this object.
- `in_is_acquirable`: A Boolean value that specifies if the box supports being acquired.
- `in_box_uid`: The name of the box, as an  .

## See Also

- [init](iouseraudiobox/init.md)
  Initializes an instance of the audio box class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/create)*