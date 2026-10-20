# endProgress

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Indicates the end point of the receiver as a fraction of the entire transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var endProgress: Float { get set }
```

```objc
@property float endProgress;
```

#### Discussion

The value must be greater than or equal to [`startProgress`](./startprogress.md), and not greater than 1.0.  If `endProgress` is less than [`startProgress`](./startprogress.md) the behavior is undefined. The default value is 1.0.

## See Also

### Transition start and end point
- [var startProgress: Float](./startprogress.md)
  Indicates the start point of the receiver as a fraction of the entire transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransition/endprogress)*