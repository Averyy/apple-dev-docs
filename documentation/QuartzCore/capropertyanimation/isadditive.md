# isAdditive

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Determines if the value specified by the animation is added to the current render tree value to produce the new render tree value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isAdditive: Bool { get set }
```

```objc
@property (getter=isAdditive) BOOL additive;
```

#### Discussion

If [`true`](../../Swift/true.md), the value specified by the animation will be added to the current render tree value of the property to produce the new render tree value. The addition function is type-dependent, e.g. for affine transforms the two matrices are concatenated. The default is [`false`](../../Swift/false.md).

## See Also

### Property Value Calculation Behavior
- [var isCumulative: Bool](./iscumulative.md)
  Determines if the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle.
- [var valueFunction: CAValueFunction?](./valuefunction.md)
  An optional value function that is applied to interpolated values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/capropertyanimation/isadditive)*