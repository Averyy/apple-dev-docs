# ChairBackType

**Framework**: RoomPlan  
**Kind**: enum

Types of chair back the framework identifies in a captured room.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ChairBackType
```

#### Overview

When the framework observes a chair in the physical environment during a scan, it chooses a type among these options that best matches the look of the chair’s back. The framework adds that instance of this enum to the [`attributes`](capturedroom/object/attributes.md) array for the object (see [`objects`](capturedroom/objects.md)) that represents the chair in the captured room.

## Topics

### Choosing a chair back type
- [ChairBackType.existing](chairbacktype/existing.md)
  A type of chair that has a back.
- [ChairBackType.missing](chairbacktype/missing.md)
  A type of chair that has no back.
### Identifying a chair back type
- [var shortIdentifier: String](chairbacktype/shortidentifier.md)
  A human-readable identifier for the attribute.
### Categorizing a chair back type
- [static var parentCategory: CapturedElementCategory?](chairbacktype/parentcategory.md)
  A category to which this room attribute belongs.
### Creating a chair back type
- [init?(rawValue: String)](chairbacktype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](chairbacktype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ChairBackType.AllCases](chairbacktype/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [ChairBackType.RawValue](chairbacktype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [ChairBackType]](chairbacktype/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](chairbacktype/equatable-implementations.md)
- [RawRepresentable Implementations](chairbacktype/rawrepresentable-implementations.md)

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
- [enum ChairArmType](chairarmtype.md)
  Types of armchair the framework identifies in a captured room.
- [enum ChairLegType](chairlegtype.md)
  Types of chair legs the framework identifies in a captured room.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/chairbacktype)*