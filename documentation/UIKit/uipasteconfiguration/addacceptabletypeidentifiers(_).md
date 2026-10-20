# addAcceptableTypeIdentifiers(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addAcceptableTypeIdentifiers(_ acceptableTypeIdentifiers: [String])
```

```objc
- (void) addAcceptableTypeIdentifiers:(NSArray<NSString *> *) acceptableTypeIdentifiers;
```

#### Discussion

List the acceptable UTIs in descending order of fidelity. The UTI that provides the richest data representation should be first in the list. For instance, if the data to paste is contact information, list the vCard UTI first, followed by the plain text UTI.

## Parameters

- `acceptableTypeIdentifiers`: An array of uniform type identifier (UTI) strings.

## See Also

### Adding acceptable type identifiers
- [func addTypeIdentifiers(forAccepting: any NSItemProviderReading.Type)](./addtypeidentifiers%28foraccepting%29-4fvd6.md)
  Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.
- [func addTypeIdentifiers<T>(forAccepting: T.Type)](./addtypeidentifiers%28foraccepting%29-8af7o.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/addacceptabletypeidentifiers(_:))*