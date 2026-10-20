# keyedUnarchiveFromDataTransformerName

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide.

**Availability**:
- iOS 3.0+ - Deprecated in 12.0 (renamed: NSValueTransformerName.secureUnarchiveFromDataTransformerName)
- iPadOS 3.0+ - Deprecated in 12.0 (renamed: NSValueTransformerName.secureUnarchiveFromDataTransformerName)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSValueTransformerName.secureUnarchiveFromDataTransformerName)
- macOS 10.3+ - Deprecated in 10.14 (renamed: NSValueTransformerName.secureUnarchiveFromDataTransformerName)
- tvOS 9.0+ - Deprecated in 12.0 (renamed: NSValueTransformerName.secureUnarchiveFromDataTransformerName)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: NSValueTransformerName.secureUnarchiveFromDataTransformerName)
- watchOS 2.0+ - Deprecated in 5.0 (renamed: NSValueTransformerName.secureUnarchiveFromDataTransformerName)

> **Deprecated**: Use [`secureUnarchiveFromDataTransformerName`](./secureunarchivefromdatatransformername.md) instead.

## Declaration

```swift
static let keyedUnarchiveFromDataTransformerName: NSValueTransformerName
```

```c
extern NSValueTransformerName const NSKeyedUnarchiveFromDataTransformerName;
```

#### Discussion

The transformer this property references returns the [`NSData`](../nsdata.md) instance created by archiving the value using keyed archiving. This transformer requires that an object implement the [`NSCoding`](../nscoding.md) protocol using keyed archiving in order to archive and unarchive with this transformer.

## See Also

### Type Properties
- [static let isNilTransformerName: NSValueTransformerName](./isniltransformername.md)
  This value transformer returns true if the value is nil.
- [static let isNotNilTransformerName: NSValueTransformerName](./isnotniltransformername.md)
  This value transformer returns true if the value is non-nil.
- [static let negateBooleanTransformerName: NSValueTransformerName](./negatebooleantransformername.md)
  This value transformer negates a boolean value, transforming true to false and false to true.
- [static let unarchiveFromDataTransformerName: NSValueTransformerName](./unarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data from an object you provide.
- [static let secureUnarchiveFromDataTransformerName: NSValueTransformerName](./secureunarchivefromdatatransformername.md)
  The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvaluetransformername/keyedunarchivefromdatatransformername)*