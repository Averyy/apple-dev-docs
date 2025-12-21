# NSFetchRequestExpression

**Framework**: Core Data  
**Kind**: class

An expression that evaluates the result of a fetch request on a managed object context.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSFetchRequestExpression
```

#### Overview

`NSFetchRequestExpression` inherits from [`NSExpression`](https://developer.apple.com/documentation/Foundation/NSExpression), which provides most of the basic behavior. The first argument must be an expression which evaluates to an `NSFetchRequest` object, and the second must be an expression which evaluates to an `NSManagedObjectContext` object. If you simply want the count for the request, the `countOnly` argument should be [`true`](https://developer.apple.com/documentation/Swift/true).

## Topics

### Creating a Fetch Request Expression
- [class func expression(forFetch: NSExpression, context: NSExpression, countOnly: Bool) -> NSExpression](nsfetchrequestexpression/expression(forfetch:context:countonly:).md)
  Returns an expression which will evaluate to the result of executing a fetch request on a context.
### Examining a Fetch Request Expression
- [var requestExpression: NSExpression](nsfetchrequestexpression/requestexpression.md)
  The expression for the receiver’s fetch request.
- [var contextExpression: NSExpression](nsfetchrequestexpression/contextexpression.md)
  The expression for the receiver’s managed object context.
- [var isCountOnlyRequest: Bool](nsfetchrequestexpression/iscountonlyrequest.md)
  Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.
### Constants
- [let NSFetchRequestExpressionType: NSExpression.ExpressionType](nsfetchrequestexpressiontype.md)
  This constant specifies the fetch request expression type.

## Relationships

### Inherits From
- [NSExpression](../Foundation/NSExpression.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var predicate: NSPredicate?](nsfetchrequest/predicate.md)
  The predicate of the fetch request.
- [var fetchLimit: Int](nsfetchrequest/fetchlimit.md)
  The fetch limit of the fetch request.
- [var fetchOffset: Int](nsfetchrequest/fetchoffset.md)
  The fetch offset of the fetch request.
- [var fetchBatchSize: Int](nsfetchrequest/fetchbatchsize.md)
  The batch size of the objects specified in the fetch request.
- [var affectedStores: [NSPersistentStore]?](nsfetchrequest/affectedstores.md)
  An array of persistent stores specified for the fetch request.
- [class NSExpressionDescription](nsexpressiondescription.md)
  An object that describes an expression to include with a fetch request.
- [class NSFetchedPropertyDescription](nsfetchedpropertydescription.md)
  A description object used to define which properties are fetched from Core Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression)*