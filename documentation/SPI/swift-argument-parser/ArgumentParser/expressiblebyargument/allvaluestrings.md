---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument/allvaluestrings"
framework: "swift-argument-parser/ArgumentParser"
---

# allValueStrings

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

An array of all possible strings that can convert to a value of this type, for display in the help screen.

## Declaration

```swift
static var allValueStrings: [String] { get }
```

## Mentions

- [Customizing Help](../customizinghelp.md)

#### Discussion

The default implementation of this property returns an empty array. If the conforming type is also `CaseIterable`, the default implementation returns an array with a value for each case.

## Default Implementations

### ExpressibleByArgument Implementations
- [static var allValueStrings: [String]](./allvaluestrings-4tymu.md)
  An array of all possible strings that can convert to a value of this type, for display in the help screen.
- [static var allValueStrings: [String]](./allvaluestrings-5keru.md)
  An array of all possible strings that can convert to a value of this type, for display in the help screen.
- [static var allValueStrings: [String]](./allvaluestrings-6ptln.md)
  An array of all possible strings that can convert to a value of this type, for display in the help screen.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument/allvaluestrings)*