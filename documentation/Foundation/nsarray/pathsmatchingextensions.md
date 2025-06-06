# pathsMatchingExtensions(_:)

**Framework**: Foundation  
**Kind**: method

Returns an array containing all the pathname elements in the receiving array that have filename extensions from a given array.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func pathsMatchingExtensions(_ filterTypes: [String]) -> [String]
```

#### Return Value

An array containing all the pathname elements in the receiving array that have filename extensions from the `filterTypes` array.

## Parameters

- `filterTypes`: An array of   objects containing filename extensions. The extensions should not include the dot (”.”) character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/pathsmatchingextensions(_:))*