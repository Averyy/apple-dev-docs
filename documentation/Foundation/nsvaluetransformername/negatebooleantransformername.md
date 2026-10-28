# negateBooleanTransformerName

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

This value transformer negates a boolean value, transforming true to false and false to true.

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

```c
extern NSValueTransformerName const NSNegateBooleanTransformerName;
```

## Discussion

This transformer is reversible.

## See Also

### Type Properties
- [static let isNilTransformerName: NSValueTransformerName](./isniltransformername.md)
  This value transformer returns true if the value is nil.
- [static let isNotNilTransformerName: NSValueTransformerName](./isnotniltransformername.md)
  This value transformer returns true if the value is non-nil.
- [static let keyedUnarchiveFromDataTransformerName: NSValueTransformerName](./keyedunarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data stored inside a keyed archive in an object you provide.
- [static let unarchiveFromDataTransformerName: NSValueTransformerName](./unarchivefromdatatransformername.md)
  The name of the value transformer that attempts to unarchive data from an object you provide.
- [static let secureUnarchiveFromDataTransformerName: NSValueTransformerName](./secureunarchivefromdatatransformername.md)
  The name of the value transformer that creates then returns an object by attempting to unarchive the data to a class that supports secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvaluetransformername/negatebooleantransformername)*