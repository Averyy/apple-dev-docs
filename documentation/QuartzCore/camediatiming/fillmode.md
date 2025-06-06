# fillMode

**Framework**: Core Animation  
**Kind**: property  
**Required**: Yes

Determines if the receiver’s presentation is frozen or removed once its active duration has completed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fillMode: CAMediaTimingFillMode { get set }
```

#### Discussion

The possible values are described in [`Fill Modes`](fill-modes.md). The default is [`removed`](camediatimingfillmode/removed.md).

## See Also

- [var autoreverses: Bool](camediatiming/autoreverses.md)
  Determines if the receiver plays in the reverse upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/fillmode)*