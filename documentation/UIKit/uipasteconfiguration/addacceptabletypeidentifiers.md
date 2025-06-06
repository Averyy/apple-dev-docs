# addAcceptableTypeIdentifiers(_:)

**Framework**: UIKit  
**Kind**: method

Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addAcceptableTypeIdentifiers(_ acceptableTypeIdentifiers: [String])
```

#### Discussion

List the acceptable UTIs in descending order of fidelity. The UTI that provides the richest data representation should be first in the list. For instance, if the data to paste is contact information, list the vCard UTI first, followed by the plain text UTI.

## Parameters

- `acceptableTypeIdentifiers`: An array of uniform type identifier (UTI) strings.

## See Also

- [func addTypeIdentifiers(forAccepting: any NSItemProviderReading.Type)](uipasteconfiguration/addtypeidentifiers(foraccepting:)-4fvd6.md)
  Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.
- [func addTypeIdentifiers<T>(forAccepting: T.Type)](uipasteconfiguration/addtypeidentifiers(foraccepting:)-8af7o.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/addacceptabletypeidentifiers(_:))*