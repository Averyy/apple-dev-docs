---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(name:defaultasflag:parsing:help:completion:)"
framework: "swift-argument-parser/ArgumentParser"
---

# init(name:defaultAsFlag:parsing:help:completion:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates an optional property that reads its value from a labeled option, with a default value when the flag is provided without a value.

## Declaration

```swift
init<T>(name: NameSpecification = .long, defaultAsFlag: T, parsing parsingStrategy: DefaultAsFlagParsingStrategy = .scanningForValue, help: ArgumentHelp? = nil, completion: CompletionKind? = nil) where Value == T?, T : ExpressibleByArgument
```

#### Discussion

This initializer allows providing a `defaultAsFlag` value that is used when the flag is present but no value follows it:

```swift
@Option(name: .customLong("bin-path"), defaultAsFlag: "/default/path")
var showBinPath: String?
```

## Parameters

- `name`: A specification for what names are allowed for this option.
- `defaultAsFlag`: The value to use when the flag is provided without a value.
- `parsingStrategy`: The behavior to use when looking for this option’s value.
- `help`: Information about how to use this option.
- `completion`: The type of command-line completion provided for this option.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(name:defaultasflag:parsing:help:completion:))*