# isCountOnlyRequest

**Framework**: Core Data  
**Kind**: property

Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.

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
var isCountOnlyRequest: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver represents a count-only fetch request, otherwise [`false`](https://developer.apple.com/documentation/swift/false). If this method returns [`false`](https://developer.apple.com/documentation/swift/false), the managed object context (from the [`contextExpression`](nsfetchrequestexpression/contextexpression.md)) will perform [`fetch(_:)`](nsmanagedobjectcontext/fetch(_:)-38ys1.md): with the [`requestExpression`](nsfetchrequestexpression/requestexpression.md); if this method returns [`true`](https://developer.apple.com/documentation/swift/true), the managed object context will perform [`count(for:)`](nsmanagedobjectcontext/count(for:)-93zbm.md) with the [`requestExpression`](nsfetchrequestexpression/requestexpression.md).

## See Also

- [var requestExpression: NSExpression](nsfetchrequestexpression/requestexpression.md)
  The expression for the receiver’s fetch request.
- [var contextExpression: NSExpression](nsfetchrequestexpression/contextexpression.md)
  The expression for the receiver’s managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/iscountonlyrequest)*