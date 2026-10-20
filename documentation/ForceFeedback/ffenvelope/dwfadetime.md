# dwFadeTime

**Framework**: Force Feedback  
**Kind**: property  
**Role**: Instance Property

The time, in microseconds, to reach the fade level.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var dwFadeTime: DWORD
```

```c
DWORD dwFadeTime;
```

## See Also

### Instance Properties
- [var dwAttackLevel: DWORD](./dwattacklevel.md)
  Amplitude for the start of the envelope, relative to the baseline, in the range from 0 through 10,000. If the effect’s type-specific data does not specify a baseline, the amplitude is relative to 0.
- [var dwAttackTime: DWORD](./dwattacktime.md)
  The time, in microseconds, to reach the sustain level.
- [var dwFadeLevel: DWORD](./dwfadelevel.md)
  Amplitude for the end of the envelope, relative to the baseline, in the range from 0 through 10,000. If the effect’s type-specific data does not specify a baseline, the amplitude is relative to 0.
- [var dwSize: DWORD](./dwsize.md)
  Size, in bytes, of this structure. This member must be initialized before the structure is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffenvelope/dwfadetime)*