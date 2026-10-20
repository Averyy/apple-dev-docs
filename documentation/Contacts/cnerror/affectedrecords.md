# affectedRecords

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

An array of record objects for which the error applies.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var affectedRecords: [AnyObject]? { get }
```

## See Also

### Error details
- [var affectedRecordIdentifiers: [String]?](./affectedrecordidentifiers.md)
  An array of strings that uniquely identify the records affected by the error.
- [CNError.Code](./code.md)
  Error codes that the system may return when you use Contacts framework methods.
- [var keyPaths: [String]?](./keypaths.md)
  An array of key paths associated with the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnerror/affectedrecords)*