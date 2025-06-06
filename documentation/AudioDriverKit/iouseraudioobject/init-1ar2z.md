# init

**Framework**: AudioDriverKit  
**Kind**: method

Initializes an instance of the audio object base class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool init(IOUserAudioDriver * in_audio_driver);
```

#### Return Value

A Boolean value that indicates the result of initialization: `true` if initialization succeeded, `false` otherwise.

#### Discussion

Always pass in the [`IOUserAudioDriver`](iouseraudiodriver.md). The no-arg initializer, [`init`](iouseraudioobject/init-26qwx.md), always returns `false`.

## Parameters

- `in_audio_driver`: The   that owns this object.

## See Also

- [init](iouseraudioobject/init-26qwx.md)
  Initializes an empty object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/init-1ar2z)*