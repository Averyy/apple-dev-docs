# autoreverses

**Framework**: Core Animation  
**Kind**: property  
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

#### Discussion

When [`true`](https://developer.apple.com/documentation/Swift/true), the receiver plays backwards after playing forwards. Defaults to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var fillMode: CAMediaTimingFillMode](camediatiming/fillmode.md)
  Determines if the receiver’s presentation is frozen or removed once its active duration has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/autoreverses)*