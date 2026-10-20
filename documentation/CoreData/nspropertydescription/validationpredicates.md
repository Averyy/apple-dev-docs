# validationPredicates

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The validation predicates of the receiver.

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
var validationPredicates: [NSPredicate] { get }
```

```objc
@property (strong, readonly) NSArray<NSPredicate *> * validationPredicates;
```

## See Also

### Supporting Validation
- [var validationWarnings: [Any]](./validationwarnings.md)
  The error strings associated with the receiver’s validation predicates.
- [func setValidationPredicates([NSPredicate]?, withValidationWarnings: [String]?)](./setvalidationpredicates%28_,withvalidationwarnings%29.md)
  Sets the validation predicates and warnings of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/validationpredicates)*