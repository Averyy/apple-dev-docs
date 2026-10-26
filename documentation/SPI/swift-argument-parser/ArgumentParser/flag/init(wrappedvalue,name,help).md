---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(wrappedvalue:name:help:)"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:name:help:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a Boolean property with default value provided by standard Swift default value syntax that reads its value from the presence of a flag.

## Declaration

```swift
init(wrappedValue: Bool, name: NameSpecification = .long, help: ArgumentHelp? = nil)
```

Available when `Value` is `Bool`.

## Parameters

- `wrappedValue`: A default value to use for this property, provided implicitly by the compiler during property wrapper initialization.
- `name`: A specification for what names are allowed for this flag.
- `help`: Information about how to use this flag.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag/init(wrappedvalue:name:help:))*