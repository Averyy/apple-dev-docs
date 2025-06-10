# keyedUnarchiveFromDataTransformerName

**Framework**: Foundation  
**Kind**: property

The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let keyedUnarchiveFromDataTransformerName: NSValueTransformerName
```

#### Discussion

The transformer this property references returns the [`NSData`](nsdata.md) instance created by archiving the value using keyed archiving. This transformer requires that an object implement the [`NSCoding`](nscoding.md) protocol using keyed archiving in order to archive and unarchive with this transformer.

## See Also

- [static let isNilTransformerName: NSValueTransformerName](nsvaluetransformername/isniltransformername.md)
  This value transformer returns [`true`](https://developer.apple.com/documentation/swift/true) if the value is `nil`.
- [static let isNotNilTransformerName: NSValueTransformerName](nsvaluetransformername/isnotniltransformername.md)
  This value transformer returns [`true`](https://developer.apple.com/documentation/swift/true) if the value is non-`nil`.
- [static let negateBooleanTransformerName: NSValueTransformerName](nsvaluetransformername/negatebooleantransformername.md)
  This value transformer negates a boolean value, transforming [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false) and [`false`](https://developer.apple.com/documentation/swift/false) to [`true`](https://developer.apple.com/documentation/swift/true).
- [static let unarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/unarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data from an object you provide.
- [static let secureUnarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/secureunarchivefromdatatransformername.md)
  The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvaluetransformername/keyedunarchivefromdatatransformername)*