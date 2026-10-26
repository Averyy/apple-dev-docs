# adjust-panner

**Framework**: Professional-Video-Applications  
**Role**: Article

Modifies the audio-panning levels.

#### Overview

Use the `adjust-panner` attributes given below to applt the audio=panning levels.

| Attribute | Description |
| --- | --- |
| `mode` | The pan mode. ![](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/spacer.png) See [Pan Modes](./adjust-panner.md#Pan-Modes) for supported values. |
| `amount` | The pan amount. |
| `original_decoded_mix` | The balance between the original and decoded signals. |
| `ambient_direct_mix` | The balance between the decoded surround and center signals. |
| `surround_width` | The separation, in dB, between the decoded surround signals. |
| `left_right_mix` | The balance between the left and right speakers. |
| `front_back_mix` | The balance between the front and back speakers. |
| `LFE_balance` | The low-frequency effects signal. |
| `rotation` | The rotation amount for the surround signals. |
| `stereo_spread` | The stereo effect amount from the left and right channels to the center and surround speakers. |
| `attenuate_collapse_mix` | The panning effect amount. |
| `center_balance` | The balance between the center and surround signals. |

##### Pan Modes

Supported values for pan modes:

- 0 (Default)
- 1 (Stereo Left/Right)
- 2 (Create Space)
- 3 (Dialogue)
- 4 (Music)
- 5 (Ambience)
- 6 (Circle)
- 7 (Rotate)
- 8 (Back to Front)
- 9 (Left Surround to Right Front)
- 10 (Right Surround to Left Front)

---

## See Also

### Audio Adjustment Elements
- [adjust-EQ](./adjust-eq.md)
  Specifies the equalization to apply to a clip.
- [adjust-humReduction](./adjust-humreduction.md)
  Applies hum reduction at the frequency, either 50 or 60 Hz, that the frequency attribute specifies.
- [adjust-loudness](./adjust-loudness.md)
  Modifies the loudness. 
- [adjust-matchEQ](./adjust-matcheq.md)
  Specifies the equalization to apply, in an internal format, to match another clip’s frequency characteristics.
- [adjust-noiseReduction](./adjust-noisereduction.md)
  Applies noise reduction with a value between 0 and 100 that the amount attribute specifies.
- [adjust-volume](./adjust-volume.md)
  Modifies the volume of a clip in dB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/adjust-panner)*