# database

**Framework**: CloudKit  
**Kind**: property

The database that the operation uses.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var database: CKDatabase? { get set }
```

#### Discussion

For operations that you execute in a custom queue, use this property to specify the target database. Setting the database also sets the corresponding container, which it inherits from [`CKOperation`](ckoperation.md). If this property’s value is `nil`, the operation targets the user’s private database.

The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabaseoperation/database)*