# One

**Framework**: RegexBuilder  
**Kind**: struct

A regex component that matches exactly one occurrence of its underlying component.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct One<Output>
```

## Topics

### Initializers
- [init(some RegexComponent<Output>)](one/init(_:).md)
  Creates a regex component that matches the given component exactly once.

## Relationships

### Conforms To
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct Optionally](optionally.md)
  A regex component that matches zero or one occurrences of its underlying component.
- [struct ZeroOrMore](zeroormore.md)
  A regex component that matches zero or more occurrences of its underlying component.
- [struct OneOrMore](oneormore.md)
  A regex component that matches one or more occurrences of its underlying component.
- [struct Repeat](repeat.md)
  A regex component that matches a selectable number of occurrences of its underlying component.
- [struct Local](local.md)
  A regex component that represents an atomic group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/one)*