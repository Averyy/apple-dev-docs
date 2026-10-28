# autoreverses

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Determines if the receiver plays in the reverse upon completion.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var autoreverses: Bool { get set }
```

```objc
@property BOOL autoreverses;
```

## Discussion

When [`true`](../../Swift/true.md), the receiver plays backwards after playing forwards. Defaults to [`false`](../../Swift/false.md).

## See Also

### Playback Modes
- [var fillMode: CAMediaTimingFillMode](./fillmode.md)
  Determines if the receiver’s presentation is frozen or removed once its active duration has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/autoreverses)*