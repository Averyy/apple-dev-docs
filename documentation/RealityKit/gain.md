# gain

**Framework**: RealityKit

A value that controls the audio volume.

#### Overview

The runtime multiplies this value by the incoming audio to produce the output signal. An asset may use this action to raise or lower the audio’s original volume.

The default value of `1.0` matches the audio’s original volume. The runtime clamps negative values to `0.0`, which mutes the audio.

##### Declaration

```other
uniform double gain = 1.0
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [audio](audio.md)
  The location of an audio file.
- [type](type.md)
  An option that controls the order in which the actions execute.
- [auralMode](auralmode.md)
  An option that controls the audio signal’s spacial dynamics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gain)*