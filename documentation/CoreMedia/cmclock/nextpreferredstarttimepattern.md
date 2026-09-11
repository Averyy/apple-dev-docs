# nextPreferredStartTimePattern()

**Framework**: Core Media  
**Kind**: method

Returns the pattern of preferred start times, such as for synchronization with an external genlock signal.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func nextPreferredStartTimePattern() -> CMClock.StartTimePattern?
```

#### Discussion

When a genlock signal is present and disciplined, this function returns a matched time pair in the near future and the delta between successive times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/nextpreferredstarttimepattern())*