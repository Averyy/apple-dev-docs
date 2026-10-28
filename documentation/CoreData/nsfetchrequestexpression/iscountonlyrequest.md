# isCountOnlyRequest

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.

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
var isCountOnlyRequest: Bool { get }
```

```objc
@property (readonly, getter=isCountOnlyRequest) BOOL countOnlyRequest;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver represents a count-only fetch request, otherwise [`false`](../../Swift/false.md). If this method returns [`false`](../../Swift/false.md), the managed object context (from the [`contextExpression`](./contextexpression.md)) will perform [`fetch(_:)`](../nsmanagedobjectcontext/fetch%28_%29-38ys1.md): with the [`requestExpression`](./requestexpression.md); if this method returns [`true`](../../Swift/true.md), the managed object context will perform [`count(for:)`](../nsmanagedobjectcontext/count%28for%29-93zbm.md) with the [`requestExpression`](./requestexpression.md).

## See Also

### Examining a Fetch Request Expression
- [var requestExpression: NSExpression](./requestexpression.md)
  The expression for the receiver’s fetch request.
- [var contextExpression: NSExpression](./contextexpression.md)
  The expression for the receiver’s managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/iscountonlyrequest)*