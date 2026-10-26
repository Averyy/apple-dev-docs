---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification/element"
framework: "swift-argument-parser/ArgumentParser"
---

# NameSpecification.Element

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

An individual property name translation.

## Declaration

```swift
struct Element
```

## Topics

### Type Properties
- [static var long: NameSpecification.Element](./element/long.md)
  Use the property’s name, converted to lowercase with words separated by hyphens.
- [static var short: NameSpecification.Element](./element/short.md)
  Use the first character of the property’s name as a short option label.
### Type Methods
- [static func customLong(String, withSingleDash: Bool) -> NameSpecification.Element](./element/customlong%28_,withsingledash%29.md)
  Use the given string instead of the property’s name.
- [static func customShort(Character, allowingJoined: Bool) -> NameSpecification.Element](./element/customshort%28_,allowingjoined%29.md)
  Use the given character as a short option label.
### Default Implementations
- [Equatable Implementations](./element/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./element/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](./element/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](./element/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Equatable
- Swift.Escapable
- Swift.ExpressibleByExtendedGraphemeClusterLiteral
- Swift.ExpressibleByStringInterpolation
- Swift.ExpressibleByStringLiteral
- Swift.ExpressibleByUnicodeScalarLiteral
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/namespecification/element)*