# recordType

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The record type to search.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
@property (copy, readonly) CKRecordType recordType;
```

#### Discussion

A query’s results include only records of the specified type. The record type is an app-specific string that you use to distinguish among the records of your app. The records of a particular type all represent different instances of the same information. For example, an employee record type might store the employee’s name, phone number, and a reference to the employee’s manager.

## See Also

### Accessing the Query Parameters
- [var predicate: NSPredicate](./predicate.md)
  The predicate to use for matching records.
- [var sortDescriptors: [NSSortDescriptor]?](./sortdescriptors.md)
  The sort descriptors for organizing the query’s results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquery/recordtype-3clp)*