# reveal

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

The layer’s content is revealed gradually in the direction specified by the transition subtype.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let reveal: CATransitionType
```

```c
extern CATransitionType const kCATransitionReveal;
```

## Discussion

The [Common Transition Subtypes](../common-transition-subtypes.md) are used with this transition.

## See Also

### Constants
- [static let fade: CATransitionType](./fade.md)
  The layer’s content fades as it becomes visible or hidden.
- [static let moveIn: CATransitionType](./movein.md)
  The layer’s content slides into place over any existing content.
- [static let push: CATransitionType](./push.md)
  The layer’s content pushes any existing content as it slides into place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransitiontype/reveal)*