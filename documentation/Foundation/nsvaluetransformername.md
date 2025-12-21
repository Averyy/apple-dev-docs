# NSValueTransformerName

**Framework**: Foundation  
**Kind**: struct

Named value transformers defined by `NSValueTransformer`.

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
struct NSValueTransformerName
```

## Topics

### Type Properties
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
- [static let secureUnarchiveFromDataTransformerName: NSValueTransformerName](nsvaluetransformername/secureunarchivefromdatatransformername.md)
  The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.
### Initializers
- [init(String)](nsvaluetransformername/init(_:).md)
- [init(rawValue: String)](nsvaluetransformername/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func setValueTransformer(ValueTransformer?, forName: NSValueTransformerName)](valuetransformer/setvaluetransformer(_:forname:).md)
  Registers the provided value transformer with a given identifier.
- [init?(forName: NSValueTransformerName)](valuetransformer/init(forname:).md)
  Returns the value transformer identified by a given identifier.
- [class func valueTransformerNames() -> [NSValueTransformerName]](valuetransformer/valuetransformernames.md)
  Returns an array of all the registered value transformers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvaluetransformername)*