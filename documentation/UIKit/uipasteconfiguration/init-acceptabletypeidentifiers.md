# init(acceptableTypeIdentifiers:)

**Framework**: UIKit  
**Kind**: init

Initializes a new paste configuration with a specified array of acceptable UTIs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(acceptableTypeIdentifiers: [String])
```

#### Return Value

A paste configuration that is initialized with the specified UTI strings.

#### Discussion

Specify the acceptable UTIs in descending order of fidelity. The UTI that provides the richest data representation should be first in the list. For instance, if the data to paste is contact information, list the vCard UTI first, followed by the plain text UTI.

## Parameters

- `acceptableTypeIdentifiers`: An array of uniform type identifier (UTI) strings.

## See Also

- [init()](uipasteconfiguration/init.md)
  Initializes a new paste configuration.
- [convenience init(forAccepting: any NSItemProviderReading.Type)](uipasteconfiguration/init(foraccepting:)-6is3h.md)
  Initializes a new paste configuration with the UTIs declared as supported by a specified class.
- [convenience init<T>(forAccepting: T.Type)](uipasteconfiguration/init(foraccepting:)-84r2r.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/init(acceptabletypeidentifiers:))*