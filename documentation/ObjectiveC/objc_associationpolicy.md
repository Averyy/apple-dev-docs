# objc_AssociationPolicy

**Framework**: Objective-C Runtime  
**Kind**: enum  
**Role**: Enumeration

Type to specify the behavior of an association.

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
enum objc_AssociationPolicy
```

```c
enum objc_AssociationPolicy : uintptr_t;
```

## Topics

### Enumeration Cases
- [objc_AssociationPolicy.OBJC_ASSOCIATION_ASSIGN](./objc_associationpolicy/objc_association_assign.md)
  Specifies an unsafe unretained reference to the associated object.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY](./objc_associationpolicy/objc_association_copy.md)
  Specifies that the associated object is copied, and that the association is made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY_NONATOMIC](./objc_associationpolicy/objc_association_copy_nonatomic.md)
  Specifies that the associated object is copied, and that the association is not made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN](./objc_associationpolicy/objc_association_retain.md)
  Specifies a strong reference to the associated object, and that the association is made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN_NONATOMIC](./objc_associationpolicy/objc_association_retain_nonatomic.md)
  Specifies a strong reference to the associated object, and that the association is not made atomically.
### Initializers
- [init?(rawValue: UInt)](./objc_associationpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_associationpolicy)*