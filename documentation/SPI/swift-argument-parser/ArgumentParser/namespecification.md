---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification"
framework: "swift-argument-parser/ArgumentParser"
---

# NameSpecification

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A specification for how to represent a property as a command-line argument label.

## Declaration

```swift
struct NameSpecification
```

#### Overview

You can specify the names for an option or flag by using either string literal syntax or using one or more of the `NameSpecification` members. For example, to specify that the `verbose` property should have the names `-v` and `--verbose`, all of the following declarations are equivalent:

```
@Flag(name: "-v --verbose")
var verbose = false

@Flag(name: .shortAndLong)
var verbose = false

@Flag(name: [.short, .long])
var verbose = false

@Flag(name: ["-v", .long])
var verbose = false
```

## Topics

### Structures
- [NameSpecification.Element](./namespecification/element.md)
  An individual property name translation.
### Initializers
- [init<S>(S)](./namespecification/init%28_%29.md)
- [init(arrayLiteral: NameSpecification.Element...)](./namespecification/init%28arrayliteral%29.md)
### Type Properties
- [static var long: NameSpecification](./namespecification/long.md)
  Use the property’s name converted to lowercase with words separated by hyphens.
- [static var short: NameSpecification](./namespecification/short.md)
  Use the first character of the property’s name as a short option label.
- [static var shortAndLong: NameSpecification](./namespecification/shortandlong.md)
  Combine the `.short` and `.long` specifications to allow both long and short labels.
### Type Methods
- [static func customLong(String, withSingleDash: Bool) -> NameSpecification](./namespecification/customlong%28_,withsingledash%29.md)
  Use the given string instead of the property’s name.
- [static func customShort(Character, allowingJoined: Bool) -> NameSpecification](./namespecification/customshort%28_,allowingjoined%29.md)
  Use the given character as a short option label.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./namespecification/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](./namespecification/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](./namespecification/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.ExpressibleByArrayLiteral
- Swift.ExpressibleByExtendedGraphemeClusterLiteral
- Swift.ExpressibleByStringInterpolation
- Swift.ExpressibleByStringLiteral
- Swift.ExpressibleByUnicodeScalarLiteral
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Property Customization
- [Customizing Help](./customizinghelp.md)
  Support your users (and yourself) by providing rich help for arguments, options, and flags.
- [struct ArgumentHelp](./argumenthelp.md)
  Help information for a command-line argument.
- [struct ArgumentVisibility](./argumentvisibility.md)
  Visibility level of an argument’s help.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification)*