# AllCases

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

A type that can represent a collection of all values of this type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
associatedtype AllCases : Collection = [Self] where Self == Self.AllCases.Element
```

## See Also

- [static var allCases: Self.AllCases](caseiterable/allcases-swift.type.property.md)
  A collection of all values of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/caseiterable/allcases-swift.associatedtype)*