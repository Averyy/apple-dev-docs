---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(help:)"
framework: "swift-argument-parser/ArgumentParser"
---

# init(help:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates an array property with no default value that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.

## Declaration

```swift
init<Element>(help: ArgumentHelp? = nil) where Value == [Element], Element : EnumerableFlag
```

## Discussion

This method is called to initialize an array `Flag` with no default value such as:

```swift
@Flag
var foo: [CustomFlagType]
```

## Parameters

- `help`: Information about how to use this flag.

## See Also

### Custom Enumerable Flags
- [init<Element>(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28exclusivity,help%29-38n7u.md)
  Creates a property that gets its value from the presence of a flag, where the allowed flags are defined by an `EnumerableFlag` type.
- [init(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28exclusivity,help%29-5fggj.md)
  Creates a property with no default value that gets its value from the presence of a flag.
- [init(wrappedValue: Value, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28wrappedvalue,exclusivity,help%29.md)
  Creates a property with a default value provided by standard Swift default value syntax that gets its value from the presence of a flag.
- [init<Element>(wrappedValue: [Element], help: ArgumentHelp?)](./init%28wrappedvalue,help%29.md)
  Creates an array property that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(help:))*