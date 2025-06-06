# dwAttackTime

**Framework**: Force Feedback  
**Kind**: property

The time, in microseconds, to reach the sustain level.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var dwAttackTime: DWORD
```

## See Also

- [var dwAttackLevel: DWORD](ffenvelope/dwattacklevel.md)
  Amplitude for the start of the envelope, relative to the baseline, in the range from 0 through 10,000. If the effect’s type-specific data does not specify a baseline, the amplitude is relative to 0.
- [var dwFadeLevel: DWORD](ffenvelope/dwfadelevel.md)
  Amplitude for the end of the envelope, relative to the baseline, in the range from 0 through 10,000. If the effect’s type-specific data does not specify a baseline, the amplitude is relative to 0.
- [var dwFadeTime: DWORD](ffenvelope/dwfadetime.md)
  The time, in microseconds, to reach the fade level.
- [var dwSize: DWORD](ffenvelope/dwsize.md)
  Size, in bytes, of this structure. This member must be initialized before the structure is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffenvelope/dwattacktime)*