# SecCEBasicConstraints

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
struct SecCEBasicConstraints
```

```c
typedef struct { ... } SecCEBasicConstraints;
```

## Topics

### Initializers
- [init()](./seccebasicconstraints/init%28%29.md)
- [init(present: Bool, critical: Bool, isCA: Bool, pathLenConstraintPresent: Bool, pathLenConstraint: UInt32)](./seccebasicconstraints/init%28present,critical,isca,pathlenconstraintpresent,pathlenconstraint%29.md)
### Instance Properties
- [var critical: Bool](./seccebasicconstraints/critical.md)
- [var isCA: Bool](./seccebasicconstraints/isca.md)
- [var pathLenConstraint: UInt32](./seccebasicconstraints/pathlenconstraint.md)
- [var pathLenConstraintPresent: Bool](./seccebasicconstraints/pathlenconstraintpresent.md)
- [var present: Bool](./seccebasicconstraints/present.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccebasicconstraints)*