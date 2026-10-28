# expression(forFetch:context:countOnly:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Returns an expression which will evaluate to the result of executing a fetch request on a context.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func expression(forFetch fetch: NSExpression, context: NSExpression, countOnly countFlag: Bool) -> NSExpression
```

```objc
+ (NSExpression *) expressionForFetch:(NSExpression *) fetch context:(NSExpression *) context countOnly:(BOOL) countFlag;
```

## Return Value

An expression which will evaluate to the result of executing a fetch request (from `fetch`) on a managed object context (from `context`).

## Parameters

- `fetch`: An expression that evaluates to an instance of `NSFetchRequest`.
- `context`: An expression that evaluates to an instance of `NSManagedObjectContext`.
- `countFlag`: If [`true`](../../Swift/true.md), when the new expression is evaluated the managed object context (from `context`) will perform [`count(for:)`](../nsmanagedobjectcontext/count%28for%29-93zbm.md) with the fetch request (from `fetch`). If [`false`](../../Swift/false.md), when the new expression is evaluated the managed object context will perform [`fetch(_:)`](../nsmanagedobjectcontext/fetch%28_%29-38ys1.md) with the fetch request.

## See Also

### Related Documentation
- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/expression(forfetch:context:countonly:))*