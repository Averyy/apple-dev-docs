# init

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes an instance of the audio object base class.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual bool init(IOUserAudioDriver *in_audio_driver);
```

#### Return Value

A Boolean value that indicates the result of initialization: `true` if initialization succeeded, `false` otherwise.

#### Discussion

Always pass in the [`IOUserAudioDriver`](../iouseraudiodriver.md). The no-arg initializer, [`init`](./init-26qwx.md), always returns `false`.

## Parameters

- `in_audio_driver`: The [`IOUserAudioDriver`](../iouseraudiodriver.md) that owns this object.

## See Also

### Creating an Audio Object
- [init](./init-26qwx.md)
  Initializes an empty object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/init-1ar2z)*