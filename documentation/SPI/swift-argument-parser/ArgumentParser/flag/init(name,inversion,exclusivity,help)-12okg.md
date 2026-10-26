---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(name:inversion:exclusivity:help:)-12okg"
framework: "swift-argument-parser/ArgumentParser"
---

# init(name:inversion:exclusivity:help:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a Boolean property with no default value that reads its value from the presence of one or more inverted flags.

## Declaration

```swift
init(name: NameSpecification = .long, inversion: FlagInversion, exclusivity: FlagExclusivity = .chooseLast, help: ArgumentHelp? = nil)
```

Available when `Value` is `Bool`.

#### Discussion

Use this initializer to create a Boolean flag with an on/off pair. With the following declaration, for example, the user can specify either `--use-https` or `--no-use-https` to set the `useHTTPS` flag to `true` or `false`, respectively.

```swift
@Flag(inversion: .prefixedNo)
var useHTTPS: Bool
```

## Parameters

- `name`: A specification for what names are allowed for this flag.
- `inversion`: The method for converting this flag’s name into an on/off pair.
- `exclusivity`: The behavior to use when an on/off pair of flags is specified.
- `help`: Information about how to use this flag.

## See Also

### Boolean Flags with Inversions
- [init(wrappedValue: Bool, name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28wrappedvalue,name,inversion,exclusivity,help%29.md)
  Creates a Boolean property with default value provided by standard Swift default value syntax that reads its value from the presence of one or more inverted flags.
- [init(name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28name,inversion,exclusivity,help%29-1h8f7.md)
  Creates a Boolean property that reads its value from the presence of one or more inverted flags.
- [struct FlagInversion](../flaginversion.md)
  The options for converting a Boolean flag into a `true`/`false` pair.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(name:inversion:exclusivity:help:)-12okg)*