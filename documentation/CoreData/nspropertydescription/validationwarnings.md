# validationWarnings

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The error strings associated with the receiver’s validation predicates.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var validationWarnings: [Any] { get }
```

```objc
@property (strong, readonly) NSArray * validationWarnings;
```

## See Also

### Supporting Validation
- [var validationPredicates: [NSPredicate]](./validationpredicates.md)
  The validation predicates of the receiver.
- [func setValidationPredicates([NSPredicate]?, withValidationWarnings: [String]?)](./setvalidationpredicates%28_,withvalidationwarnings%29.md)
  Sets the validation predicates and warnings of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/validationwarnings)*