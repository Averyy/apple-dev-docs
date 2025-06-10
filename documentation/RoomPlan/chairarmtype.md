# ChairArmType

**Framework**: RoomPlan  
**Kind**: enum

Types of armchair the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ChairArmType
```

#### Overview

When the framework observes a chair in the physical environment during a scan, it chooses a type among these options that best matches the look of the chair’s arms. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the chair in the captured room.

## Topics

### Choosing a chair arm type
- [ChairArmType.existing](chairarmtype/existing.md)
  A type of chair that has arms.
- [ChairArmType.missing](chairarmtype/missing.md)
  A type of chair with no arms.
### Identifying a chair arm type
- [var shortIdentifier: String](chairarmtype/shortidentifier.md)
  A human-readable identifier for the attribute.
### Categorizing a chair arm type
- [static var parentCategory: CapturedElementCategory?](chairarmtype/parentcategory.md)
  A category to which this room attribute belongs.
### Creating a chair arm type
- [init?(rawValue: String)](chairarmtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](chairarmtype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ChairArmType.AllCases](chairarmtype/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [ChairArmType.RawValue](chairarmtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [ChairArmType]](chairarmtype/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](chairarmtype/equatable-implementations.md)
- [RawRepresentable Implementations](chairarmtype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CapturedRoomAttribute](capturedroomattribute.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ChairType](chairtype.md)
  Types of chair that the framework identifies in a captured room.
- [enum ChairLegType](chairlegtype.md)
  Types of chair legs the framework identifies in a captured room.
- [enum ChairBackType](chairbacktype.md)
  Types of chair back the framework identifies in a captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/chairarmtype)*