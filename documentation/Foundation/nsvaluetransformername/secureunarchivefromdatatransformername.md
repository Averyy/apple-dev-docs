# secureUnarchiveFromDataTransformerName

**Framework**: Foundation  
**Kind**: property

The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static let secureUnarchiveFromDataTransformerName: NSValueTransformerName
```

#### Discussion

The transformer this property references returns the [`NSData`](nsdata.md) instance created by archiving the value using secure keyed archiving. This transformer requires that an object implement the [`NSSecureCoding`](nssecurecoding.md) protocol in order to archive and unarchive with this transformer.

## See Also

- [static let isNilTransformerName: NSValueTransformerName](nsvaluetransformername/isniltransformername.md)
  This value transformer returns true if the value is nil.
- [static let isNotNilTransformerName: NSValueTransformerName](nsvaluetransformername/isnotniltransformername.md)
  This value transformer returns true if the value is non-nil.
- [static let keyedUnarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/keyedunarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide.
- [static let negateBooleanTransformerName: NSValueTransformerName](nsvaluetransformername/negatebooleantransformername.md)
  This value transformer negates a boolean value, transforming true to false and false to true.
- [static let unarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/unarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data from an object you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvaluetransformername/secureunarchivefromdatatransformername)*