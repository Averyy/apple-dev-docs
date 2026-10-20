# CMTimebaseCopySource(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the immediate source — either a clock or timebase — of a timebase.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimebaseCopySource(_ timebase: CMTimebase) -> CMClockOrTimebase
```

```c
extern CMClockOrTimebaseRefCMTimebaseCopySource(CMTimebaseRef timebase);
```

## See Also

### Copying Timebases
- [func CMTimebaseCopySourceClock(CMTimebase) -> CMClock?](./cmtimebasecopysourceclock%28_%29.md)
  Returns the immediate source clock of a timebase.
- [func CMTimebaseCopySourceTimebase(CMTimebase) -> CMTimebase?](./cmtimebasecopysourcetimebase%28_%29.md)
  Returns the immediate source timebase of a timebase.
- [func CMTimebaseCopyUltimateSourceClock(CMTimebase) -> CMClock](./cmtimebasecopyultimatesourceclock%28_%29.md)
  Returns the source clock that’s the source of all of a timebase’s source timebases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimebasecopysource(_:))*