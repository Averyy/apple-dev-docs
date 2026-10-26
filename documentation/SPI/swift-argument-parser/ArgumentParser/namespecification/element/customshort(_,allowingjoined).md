---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification/element/customshort(_:allowingjoined:)"
framework: "swift-argument-parser/ArgumentParser"
---

# customShort(_:allowingJoined:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Use the given character as a short option label.

## Declaration

```swift
static func customShort(_ char: Character, allowingJoined: Bool = false) -> NameSpecification.Element
```

#### Return Value

A `short` name specification with the requested `char`.

#### Discussion

When passing `true` as `allowingJoined` in an `@Option` declaration, the user can join a value with the option name. For example, if an option is declared as `-D`, allowing joined values, a user could pass `-Ddebug` to specify `debug` as the value for that option.

## Parameters

- `char`: The name of the option or flag.
- `allowingJoined`: A Boolean value indicating whether this short name allows a joined value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification/element/customshort(_:allowingjoined:))*