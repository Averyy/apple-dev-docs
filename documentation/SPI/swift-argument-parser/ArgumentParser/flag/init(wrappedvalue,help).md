---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(wrappedvalue:help:)"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:help:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates an array property that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.

## Declaration

```swift
init<Element>(wrappedValue: [Element], help: ArgumentHelp? = nil) where Value == [Element], Element : EnumerableFlag
```

#### Discussion

This property has an empty array as its default value.

## Parameters

- `wrappedValue`: A default value to use for this property, provided
- `help`: Information about how to use this flag.

## See Also

### Custom Enumerable Flags
- [init<Element>(help: ArgumentHelp?)](./init%28help%29.md)
  Creates an array property with no default value that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.
- [init<Element>(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28exclusivity,help%29-38n7u.md)
  Creates a property that gets its value from the presence of a flag, where the allowed flags are defined by an `EnumerableFlag` type.
- [init(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28exclusivity,help%29-5fggj.md)
  Creates a property with no default value that gets its value from the presence of a flag.
- [init(wrappedValue: Value, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28wrappedvalue,exclusivity,help%29.md)
  Creates a property with a default value provided by standard Swift default value syntax that gets its value from the presence of a flag.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(wrappedvalue:help:))*