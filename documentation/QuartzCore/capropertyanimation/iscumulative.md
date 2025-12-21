# isCumulative

**Framework**: Core Animation  
**Kind**: property

Determines if the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isCumulative: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), then the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle. If [`false`](https://developer.apple.com/documentation/Swift/false), the value of the property is simply the value calculated for the current repeat cycle. The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isAdditive: Bool](capropertyanimation/isadditive.md)
  Determines if the value specified by the animation is added to the current render tree value to produce the new render tree value.
- [var valueFunction: CAValueFunction?](capropertyanimation/valuefunction.md)
  An optional value function that is applied to interpolated values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/capropertyanimation/iscumulative)*