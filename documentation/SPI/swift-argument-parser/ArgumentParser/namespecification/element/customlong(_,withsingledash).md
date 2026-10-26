---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification/element/customlong(_:withsingledash:)"
framework: "swift-argument-parser/ArgumentParser"
---

# customLong(_:withSingleDash:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Use the given string instead of the property’s name.

## Declaration

```swift
static func customLong(_ name: String, withSingleDash: Bool = false) -> NameSpecification.Element
```

#### Return Value

A `long` name specification with the requested `name`.

#### Discussion

To create a single-dash argument, pass `true` as `withSingleDash`. Note that combining single-dash options and options with short, single-character names can lead to ambiguities for the user.

## Parameters

- `name`: The name of the option or flag.
- `withSingleDash`: A Boolean value indicating whether to use a single dash as the prefix. If `false`, the name has a double-dash prefix.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification/element/customlong(_:withsingledash:))*