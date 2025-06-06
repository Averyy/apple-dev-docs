# ChairType

**Framework**: RoomPlan  
**Kind**: enum

Types of chair that the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ChairType
```

#### Overview

When the framework observes a chair in the physical environment during a scan, it chooses a type among these options that best matches the chair’s look. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the chair in the captured room.

## Topics

### Choosing a chair type
- [ChairType.dining](chairtype/dining.md)
  A type of chair that accompanies a dining table.
- [ChairType.stool](chairtype/stool.md)
  A type of chair that resembles a stool.
- [ChairType.swivel](chairtype/swivel.md)
  A type of chair that swivels.
- [ChairType.unidentified](chairtype/unidentified.md)
  An uncategorized chair type.
### Identifying a chair type
- [var shortIdentifier: String](chairtype/shortidentifier.md)
  A human-readable identifier for the attribute.
### Categorizing a chair type
- [static var parentCategory: CapturedElementCategory?](chairtype/parentcategory.md)
  A category to which this room attribute belongs.
### Creating a chair type
- [init?(rawValue: String)](chairtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](chairtype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ChairType.AllCases](chairtype/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [ChairType.RawValue](chairtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [ChairType]](chairtype/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](chairtype/equatable-implementations.md)
- [RawRepresentable Implementations](chairtype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CapturedRoomAttribute](capturedroomattribute.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum ChairArmType](chairarmtype.md)
  Types of armchair the framework identifies in a captured room.
- [enum ChairLegType](chairlegtype.md)
  Types of chair legs the framework identifies in a captured room.
- [enum ChairBackType](chairbacktype.md)
  Types of chair back the framework identifies in a captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/chairtype)*