# negateBooleanTransformerName

**Framework**: Foundation  
**Kind**: property

This value transformer negates a boolean value, transforming [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false) and [`false`](https://developer.apple.com/documentation/swift/false) to [`true`](https://developer.apple.com/documentation/swift/true).

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
static let negateBooleanTransformerName: NSValueTransformerName
```

#### Discussion

This transformer is reversible.

## See Also

- [static let isNilTransformerName: NSValueTransformerName](nsvaluetransformername/isniltransformername.md)
  This value transformer returns [`true`](https://developer.apple.com/documentation/swift/true) if the value is `nil`.
- [static let isNotNilTransformerName: NSValueTransformerName](nsvaluetransformername/isnotniltransformername.md)
  This value transformer returns [`true`](https://developer.apple.com/documentation/swift/true) if the value is non-`nil`.
- [static let keyedUnarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/keyedunarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide.
- [static let unarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/unarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data from an object you provide.
- [static let secureUnarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/secureunarchivefromdatatransformername.md)
  The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvaluetransformername/negatebooleantransformername)*