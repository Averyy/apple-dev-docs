# repeatCount

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property float repeatCount;
```

## Discussion

May be fractional. If the `repeatCount` is 0, it is ignored. Defaults to 0. If both [`repeatDuration`](./repeatduration.md) and [`repeatCount`](./repeatcount.md) are specified the behavior is undefined.

Setting this property to [`greatestFiniteMagnitude`](../../Swift/float/greatestfinitemagnitude.md) will cause the animation to repeat forever.

## See Also

### Repeating Animations
- [var repeatDuration: CFTimeInterval](./repeatduration.md)
  Determines how many seconds the animation will repeat for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/repeatcount)*