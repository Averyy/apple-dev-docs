# NSValueTransformerName

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSValueTransformerName;
```

## Topics

### Type Properties
- [static let isNilTransformerName: NSValueTransformerName](./nsvaluetransformername/isniltransformername.md)
  This value transformer returns true if the value is nil.
- [static let isNotNilTransformerName: NSValueTransformerName](./nsvaluetransformername/isnotniltransformername.md)
  This value transformer returns true if the value is non-nil.
- [static let keyedUnarchiveFromDataTransformerName: NSValueTransformerName](./nsvaluetransformername/keyedunarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide.
- [static let negateBooleanTransformerName: NSValueTransformerName](./nsvaluetransformername/negatebooleantransformername.md)
  This value transformer negates a boolean value, transforming true to false and false to true.
- [static let unarchiveFromDataTransformerName: NSValueTransformerName](./nsvaluetransformername/unarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data from an object you provide.
- [static let secureUnarchiveFromDataTransformerName: NSValueTransformerName](./nsvaluetransformername/secureunarchivefromdatatransformername.md)
  The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.
### Initializers
- [init(String)](./nsvaluetransformername/init%28_%29.md)
- [init(rawValue: String)](./nsvaluetransformername/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Using the Name-Based Registry
- [class func setValueTransformer(ValueTransformer?, forName: NSValueTransformerName)](./valuetransformer/setvaluetransformer%28_,forname%29.md)
  Registers the provided value transformer with a given identifier.
- [init?(forName: NSValueTransformerName)](./valuetransformer/init%28forname%29.md)
  Returns the value transformer identified by a given identifier.
- [class func valueTransformerNames() -> [NSValueTransformerName]](./valuetransformer/valuetransformernames%28%29.md)
  Returns an array of all the registered value transformers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvaluetransformername)*