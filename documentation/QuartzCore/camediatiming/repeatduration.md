# repeatDuration

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property CFTimeInterval repeatDuration;
```

#### Discussion

Defaults to 0. If the `repeatDuration` is 0, it is ignored. If both [`repeatDuration`](./repeatduration.md) and [`repeatCount`](./repeatcount.md) are specified the behavior is undefined.

## See Also

### Repeating Animations
- [var repeatCount: Float](./repeatcount.md)
  Determines the number of times the animation will repeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/repeatduration)*