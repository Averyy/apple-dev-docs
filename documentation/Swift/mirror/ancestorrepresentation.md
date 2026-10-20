# Mirror.AncestorRepresentation

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

The representation to use for ancestor classes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AncestorRepresentation
```

#### Overview

A class that conforms to the `CustomReflectable` protocol can control how its mirror represents ancestor classes by initializing the mirror with an `AncestorRepresentation`. This setting has no effect on mirrors reflecting value type instances.

## Topics

### Enumeration Cases
- [Mirror.AncestorRepresentation.customized(_:)](./ancestorrepresentation/customized%28_%29.md)
  Uses the nearest ancestor’s implementation of `customMirror` to create a mirror for that ancestor.
- [Mirror.AncestorRepresentation.generated](./ancestorrepresentation/generated.md)
  Generates a default mirror for all ancestor classes.
- [Mirror.AncestorRepresentation.suppressed](./ancestorrepresentation/suppressed.md)
  Suppresses the representation of all ancestor classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror/ancestorrepresentation)*