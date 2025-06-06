# JournalingSuggestion.MotionActivity.MovementType

**Framework**: Journaling Suggestions  
**Kind**: struct

The movement activity type that the phone records when it detects motion.

**Availability**:
- iOS 18.0+

## Declaration

```swift
struct MovementType
```

## Topics

### Recording movement type
- [static let running: JournalingSuggestion.MotionActivity.MovementType](journalingsuggestion/motionactivity/movementtype-swift.struct/running.md)
  A running movement activity type.
- [static let runningWalking: JournalingSuggestion.MotionActivity.MovementType](journalingsuggestion/motionactivity/movementtype-swift.struct/runningwalking.md)
  A mixed running and walking movement activity type.
- [static let walking: JournalingSuggestion.MotionActivity.MovementType](journalingsuggestion/motionactivity/movementtype-swift.struct/walking.md)
  A walking movement activity type.
### Decoding a value
- [init(from: any Decoder) throws](journalingsuggestion/motionactivity/movementtype-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (JournalingSuggestion.MotionActivity.MovementType, JournalingSuggestion.MotionActivity.MovementType) -> Bool](journalingsuggestion/motionactivity/movementtype-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](journalingsuggestion/motionactivity/movementtype-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](journalingsuggestion/motionactivity/movementtype-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](journalingsuggestion/motionactivity/movementtype-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](journalingsuggestion/motionactivity/movementtype-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var steps: Int](journalingsuggestion/motionactivity/steps.md)
  The number of steps a person takes.
- [var movementType: JournalingSuggestion.MotionActivity.MovementType?](journalingsuggestion/motionactivity/movementtype-swift.property.md)
  The specific type of movement associated with the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/motionactivity/movementtype-swift.struct)*