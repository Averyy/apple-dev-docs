# repeatCount

**Framework**: Core Animation  
**Kind**: property  
**Required**: Yes

Determines the number of times the animation will repeat.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var repeatCount: Float { get set }
```

#### Discussion

May be fractional. If the `repeatCount` is 0, it is ignored. Defaults to 0. If both [`repeatDuration`](camediatiming/repeatduration.md) and [`repeatCount`](camediatiming/repeatcount.md) are specified the behavior is undefined.

Setting this property to [`greatestFiniteMagnitude`](https://developer.apple.com/documentation/Swift/Float/greatestFiniteMagnitude) will cause the animation to repeat forever.

## See Also

- [var repeatDuration: CFTimeInterval](camediatiming/repeatduration.md)
  Determines how many seconds the animation will repeat for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/repeatcount)*