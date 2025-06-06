# objc_AssociationPolicy.OBJC_ASSOCIATION_ASSIGN

**Framework**: Objective-C Runtime  
**Kind**: case

Specifies an unsafe unretained reference to the associated object.

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
case OBJC_ASSOCIATION_ASSIGN
```

## See Also

- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY](objc_associationpolicy/objc_association_copy.md)
  Specifies that the associated object is copied, and that the association is made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY_NONATOMIC](objc_associationpolicy/objc_association_copy_nonatomic.md)
  Specifies that the associated object is copied, and that the association is not made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN](objc_associationpolicy/objc_association_retain.md)
  Specifies a strong reference to the associated object, and that the association is made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN_NONATOMIC](objc_associationpolicy/objc_association_retain_nonatomic.md)
  Specifies a strong reference to the associated object, and that the association is not made atomically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_assign)*