# init(keyframeValues:times:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a keyframe sequence with an initial set of values and times.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(keyframeValues values: [Any], times: [NSNumber])
```

```objc
- (instancetype) initWithKeyframeValues:(NSArray *) values times:(NSArray<NSNumber *> *) times;
```

## Return Value

A newly initialized sequence.

## Discussion

The two arrays must have an identical number of elements. The keyframes in the new sequence are stored in the same order as the input arrays.

## Parameters

- `values`: An array of value objects that define the keyframe values for the sequence.
- `times`: An array of [`NSNumber`](../../Foundation/nsnumber.md) objects containing floating-point values that specify the time values for the keyframes.

## See Also

### First Steps
- [Using Keyframe Sequence to effect Custom Interpolation](../using-keyframe-sequence-to-effect-custom-interpolation.md)
  See a few examples of what keyframe sequence can do.
- [convenience init(capacity: Int)](./init%28capacity%29.md)
  Initializes a new keyframe sequence.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence/init(keyframevalues:times:))*