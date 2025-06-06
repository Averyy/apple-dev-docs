# affectedRecordIdentifiers

**Framework**: Contacts  
**Kind**: property

An array of strings that uniquely identify the records affected by the error.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var affectedRecordIdentifiers: [String]? { get }
```

## See Also

- [var affectedRecords: [AnyObject]?](cnerror/affectedrecords.md)
  An array of record objects for which the error applies.
- [CNError.Code](cnerror/code.md)
  Error codes that the system may return when you use Contacts framework methods.
- [var keyPaths: [String]?](cnerror/keypaths.md)
  An array of key paths associated with the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerror/affectedrecordidentifiers)*