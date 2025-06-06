# speed

**Framework**: Core Animation  
**Kind**: property  
**Required**: Yes

Specifies how time is mapped to receiver’s time space from the parent time space.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var speed: Float { get set }
```

#### Discussion

For example, if `speed` is 2.0 local time progresses twice as fast as parent time. Defaults to 1.0.

## See Also

- [var duration: CFTimeInterval](camediatiming/duration.md)
  Specifies the basic duration of the animation, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatiming/speed)*