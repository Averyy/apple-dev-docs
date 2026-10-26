---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(exclusivity:help:)-5fggj"
framework: "swift-argument-parser/ArgumentParser"
---

# init(exclusivity:help:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a property with no default value that gets its value from the presence of a flag.

## Declaration

```swift
init(exclusivity: FlagExclusivity = .exclusive, help: ArgumentHelp? = nil)
```

Available when `Value` conforms to `EnumerableFlag`.

#### Discussion

Use this initializer to customize the name and number of states further than using a `Bool`. To use, define an `EnumerableFlag` enumeration with a case for each state, and use that as the type for your flag. In this case, the user can specify either `--use-production-server` or `--use-development-server` to set the flag’s value.

```swift
enum ServerChoice: EnumerableFlag {
  case useProductionServer
  case useDevelopmentServer
}

@Flag var serverChoice: ServerChoice
```

## Parameters

- `exclusivity`: The behavior to use when multiple flags are specified.
- `help`: Information about how to use this flag.

## See Also

### Custom Enumerable Flags
- [init<Element>(help: ArgumentHelp?)](./init%28help%29.md)
  Creates an array property with no default value that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.
- [init<Element>(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28exclusivity,help%29-38n7u.md)
  Creates a property that gets its value from the presence of a flag, where the allowed flags are defined by an `EnumerableFlag` type.
- [init(wrappedValue: Value, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28wrappedvalue,exclusivity,help%29.md)
  Creates a property with a default value provided by standard Swift default value syntax that gets its value from the presence of a flag.
- [init<Element>(wrappedValue: [Element], help: ArgumentHelp?)](./init%28wrappedvalue,help%29.md)
  Creates an array property that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(exclusivity:help:)-5fggj)*