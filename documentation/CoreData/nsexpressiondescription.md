# NSExpressionDescription

**Framework**: Core Data  
**Kind**: class

An object that describes an expression to include with a fetch request.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSExpressionDescription
```

#### Overview

An expression description describes a value that a fetch request returns, which doesn’t appear as an attribute or relationship on an entity. For example, expressions can aggregate data, or  transform an attribute’s value. You add expression descriptions to a fetch request using the [`propertiesToFetch`](nsfetchrequest/propertiestofetch.md) method.

> ❗ **Important**:  Don’t add expression descriptions to the [`properties`](nsentitydescription/properties.md) array of [`NSEntityDescription`](nsentitydescription.md).

 Don’t add expression descriptions to the [`properties`](nsentitydescription/properties.md) array of [`NSEntityDescription`](nsentitydescription.md).

## Topics

### Configuring the Expression Description
- [var expression: NSExpression?](nsexpressiondescription/expression.md)
  The expression to evaluate.
- [var resultType: NSAttributeDescription.AttributeType](nsexpressiondescription/resulttype.md)
  The attribute type of the expression’s result.
- [var expressionResultType: NSAttributeType](nsexpressiondescription/expressionresulttype.md)
  The attribute type of the expression’s result.
### Deprecated
- [Deprecated Symbols](nsexpressiondescription-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSPropertyDescription](nspropertydescription.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [class NSFetchRequestExpression](nsfetchrequestexpression.md)
  An expression that evaluates the result of a fetch request on a managed object context.
- [class NSFetchedPropertyDescription](nsfetchedpropertydescription.md)
  A description object used to define which properties are fetched from Core Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsexpressiondescription)*