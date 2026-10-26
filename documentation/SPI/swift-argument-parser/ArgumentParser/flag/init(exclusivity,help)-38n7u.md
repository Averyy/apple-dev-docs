---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(exclusivity:help:)-38n7u"
framework: "swift-argument-parser/ArgumentParser"
---

# init(exclusivity:help:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a property that gets its value from the presence of a flag, where the allowed flags are defined by an `EnumerableFlag` type.

## Declaration

```swift
init<Element>(exclusivity: FlagExclusivity = .exclusive, help: ArgumentHelp? = nil) where Value == Element?, Element : EnumerableFlag
```

## See Also

### Custom Enumerable Flags
- [init<Element>(help: ArgumentHelp?)](./init%28help%29.md)
  Creates an array property with no default value that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.
- [init(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28exclusivity,help%29-5fggj.md)
  Creates a property with no default value that gets its value from the presence of a flag.
- [init(wrappedValue: Value, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./init%28wrappedvalue,exclusivity,help%29.md)
  Creates a property with a default value provided by standard Swift default value syntax that gets its value from the presence of a flag.
- [init<Element>(wrappedValue: [Element], help: ArgumentHelp?)](./init%28wrappedvalue,help%29.md)
  Creates an array property that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(exclusivity:help:)-38n7u)*