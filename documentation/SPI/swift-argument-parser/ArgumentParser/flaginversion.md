---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flaginversion"
framework: "swift-argument-parser/ArgumentParser"
---

# FlagInversion

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

The options for converting a Boolean flag into a `true`/`false` pair.

## Declaration

```swift
struct FlagInversion
```

## Topics

### Type Properties
- [static var prefixedEnableDisable: FlagInversion](./flaginversion/prefixedenabledisable.md)
  Uses matching flags with `enable-` and `disable-` prefixes.
- [static var prefixedNo: FlagInversion](./flaginversion/prefixedno.md)
  Adds a matching flag with a `no-` prefix to represent `false`.
### Default Implementations
- [Equatable Implementations](./flaginversion/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Boolean Flags with Inversions
- [init(wrappedValue: Bool, name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28wrappedvalue,name,inversion,exclusivity,help%29.md)
  Creates a Boolean property with default value provided by standard Swift default value syntax that reads its value from the presence of one or more inverted flags.
- [init(name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28name,inversion,exclusivity,help%29-12okg.md)
  Creates a Boolean property with no default value that reads its value from the presence of one or more inverted flags.
- [init(name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28name,inversion,exclusivity,help%29-1h8f7.md)
  Creates a Boolean property that reads its value from the presence of one or more inverted flags.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flaginversion)*