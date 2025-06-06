# init

**Framework**: AudioDriverKit  
**Kind**: method

Initializes an instance of the audio box class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool init(IOUserAudioDriver * in_driver, bool in_is_acquirable, OSString * in_box_uid);
```

#### Return Value

`true` if initialization succeeded; `false` otherwise.

#### Discussion

Always pass in the [`IOUserAudioDriver`](iouseraudiodriver.md) and arguments. The no-argument ``IOUserAudioBox/init```()`always returns`false`.

## Parameters

- `in_driver`: The   that owns this object.
- `in_is_acquirable`: A Boolean value that specifies if the box supports being acquired.
- `in_box_uid`: The name of the box, as an  .

## See Also

- [Create](iouseraudiobox/create.md)
  Allocates and initializes an instance of the audio box class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/init)*