# contextExpression

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The expression for the receiver’s managed object context.

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
var contextExpression: NSExpression { get }
```

```objc
@property (strong, readonly) NSExpression * contextExpression;
```

## Discussion

The expression must evaluate to an [`NSManagedObjectContext`](../nsmanagedobjectcontext.md) object.

## See Also

### Examining a Fetch Request Expression
- [var requestExpression: NSExpression](./requestexpression.md)
  The expression for the receiver’s fetch request.
- [var isCountOnlyRequest: Bool](./iscountonlyrequest.md)
  Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/contextexpression)*