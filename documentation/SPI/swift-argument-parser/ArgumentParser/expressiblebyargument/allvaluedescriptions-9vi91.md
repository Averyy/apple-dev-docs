---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument/allvaluedescriptions-9vi91"
framework: "swift-argument-parser/ArgumentParser"
---

# allValueDescriptions

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

A dictionary containing the descriptions for each possible value of this type, for display in the help screen.

## Declaration

```swift
static var allValueDescriptions: [String : String] { get }
```

Available when `Self` conforms to `CaseIterable`, `Self` conforms to `RawRepresentable`, and `RawValue` conforms to `ExpressibleByArgument`.

#### Discussion

The default implementation of this property returns an empty dictionary. If the conforming type is also `CaseIterable`, the default implementation returns a dictionary with a description for each value as its key-value pair. Note that the conforming type must implement the `defaultValueDescription` for each value - if the description and the value are the same string, it’s assumed that a description is not implemented.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/expressiblebyargument/allvaluedescriptions-9vi91)*