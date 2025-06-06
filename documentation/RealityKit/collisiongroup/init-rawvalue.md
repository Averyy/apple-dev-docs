# init(rawValue:)

**Framework**: RealityKit  
**Kind**: init

Creates a collision group from a raw value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
init(rawValue: UInt32)
```

#### Discussion

This initializer succeeds even if the value passed as `rawValue` exceeds the static properties declared as part of the option set. Usually, you will want to create each collision groups setting a different bit flag for each value, so that multiple individual groups can be combined using [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) methods.

Here is an example of creating four collision groups using different bitflag values for each one.

```swift
let redGroup = CollisionGroup(rawValue: 1 << 0)
let blueGroup = CollisionGroup(rawValue: 1 << 1)
let greenGroup = CollisionGroup(rawValue: 1 << 2)
let yellowGroup = CollisionGroup(rawValue: 1 << 3)
```

## Parameters

- `rawValue`: The raw value of the option set to create. Each bit of   rawValue potentially represents an element of the option set, though raw   values may include bits that are not defined as distinct values of the   OptionSet type.

## See Also

- [init()](collisiongroup/init.md)
  Creates an empty option set.
- [init<S>(S)](collisiongroup/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](collisiongroup/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisiongroup/init(rawvalue:))*