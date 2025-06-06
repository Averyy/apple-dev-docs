# repeatDuration

**Framework**: Core Animation  
**Kind**: property  
**Required**: Yes

Determines how many seconds the animation will repeat for.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var repeatDuration: CFTimeInterval { get set }
```

#### Discussion

Defaults to 0. If the `repeatDuration` is 0, it is ignored. If both [`repeatDuration`](camediatiming/repeatduration.md) and [`repeatCount`](camediatiming/repeatcount.md) are specified the behavior is undefined.

## See Also

- [var repeatCount: Float](camediatiming/repeatcount.md)
  Determines the number of times the animation will repeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/repeatduration)*