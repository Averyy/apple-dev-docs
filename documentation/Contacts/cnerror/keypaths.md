# keyPaths

**Framework**: Contacts  
**Kind**: property

An array of key paths associated with the error.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var keyPaths: [String]? { get }
```

#### Discussion

For validation errors, this contains key paths to specific object properties.

## See Also

- [var affectedRecordIdentifiers: [String]?](cnerror/affectedrecordidentifiers.md)
  An array of strings that uniquely identify the records affected by the error.
- [var affectedRecords: [AnyObject]?](cnerror/affectedrecords.md)
  An array of record objects for which the error applies.
- [CNError.Code](cnerror/code.md)
  Error codes that the system may return when you use Contacts framework methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerror/keypaths)*