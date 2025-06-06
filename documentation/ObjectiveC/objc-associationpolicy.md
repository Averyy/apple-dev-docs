# objc_AssociationPolicy

**Framework**: Objective-C Runtime  
**Kind**: enum

Type to specify the behavior of an association.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum objc_AssociationPolicy
```

## Topics

### Enumeration Cases
- [objc_AssociationPolicy.OBJC_ASSOCIATION_ASSIGN](objc_associationpolicy/objc_association_assign.md)
  Specifies an unsafe unretained reference to the associated object.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY](objc_associationpolicy/objc_association_copy.md)
  Specifies that the associated object is copied, and that the association is made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY_NONATOMIC](objc_associationpolicy/objc_association_copy_nonatomic.md)
  Specifies that the associated object is copied, and that the association is not made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN](objc_associationpolicy/objc_association_retain.md)
  Specifies a strong reference to the associated object, and that the association is made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN_NONATOMIC](objc_associationpolicy/objc_association_retain_nonatomic.md)
  Specifies a strong reference to the associated object, and that the association is not made atomically.
### Initializers
- [init?(rawValue: UInt)](objc_associationpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_associationpolicy)*