# SecCEPolicyConstraints

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
struct SecCEPolicyConstraints
```

```c
typedef struct { ... } SecCEPolicyConstraints;
```

## Topics

### Initializers
- [init()](./seccepolicyconstraints/init%28%29.md)
- [init(present: Bool, critical: Bool, requireExplicitPolicyPresent: Bool, requireExplicitPolicy: UInt32, inhibitPolicyMappingPresent: Bool, inhibitPolicyMapping: UInt32)](./seccepolicyconstraints/init%28present,critical,requireexplicitpolicypresent,requireexplicitpolicy,inhibitpolicymappingpresent,inhibitpolicymapping%29.md)
### Instance Properties
- [var critical: Bool](./seccepolicyconstraints/critical.md)
- [var inhibitPolicyMapping: UInt32](./seccepolicyconstraints/inhibitpolicymapping.md)
- [var inhibitPolicyMappingPresent: Bool](./seccepolicyconstraints/inhibitpolicymappingpresent.md)
- [var present: Bool](./seccepolicyconstraints/present.md)
- [var requireExplicitPolicy: UInt32](./seccepolicyconstraints/requireexplicitpolicy.md)
- [var requireExplicitPolicyPresent: Bool](./seccepolicyconstraints/requireexplicitpolicypresent.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccepolicyconstraints)*