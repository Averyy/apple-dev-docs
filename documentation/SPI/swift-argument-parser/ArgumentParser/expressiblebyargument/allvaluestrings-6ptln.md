---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument/allvaluestrings-6ptln"
framework: "swift-argument-parser/ArgumentParser"
---

# allValueStrings

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

An array of all possible strings that can convert to a value of this type, for display in the help screen.

## Declaration

```swift
static var allValueStrings: [String] { get }
```

Available when `Self` conforms to `CaseIterable`.

#### Discussion

The default implementation of this property returns an empty array. If the conforming type is also `CaseIterable`, the default implementation returns an array with a value for each case.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument/allvaluestrings-6ptln)*