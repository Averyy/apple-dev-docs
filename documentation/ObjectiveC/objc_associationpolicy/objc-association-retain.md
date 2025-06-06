# objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN

**Framework**: Objective-C Runtime  
**Kind**: case

Specifies a strong reference to the associated object, and that the association is made atomically.

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
case OBJC_ASSOCIATION_RETAIN
```

## See Also

- [objc_AssociationPolicy.OBJC_ASSOCIATION_ASSIGN](objc_associationpolicy/objc_association_assign.md)
  Specifies an unsafe unretained reference to the associated object.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY](objc_associationpolicy/objc_association_copy.md)
  Specifies that the associated object is copied, and that the association is made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_COPY_NONATOMIC](objc_associationpolicy/objc_association_copy_nonatomic.md)
  Specifies that the associated object is copied, and that the association is not made atomically.
- [objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN_NONATOMIC](objc_associationpolicy/objc_association_retain_nonatomic.md)
  Specifies a strong reference to the associated object, and that the association is not made atomically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_retain)*