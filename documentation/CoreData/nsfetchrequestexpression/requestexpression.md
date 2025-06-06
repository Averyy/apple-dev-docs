# requestExpression

**Framework**: Core Data  
**Kind**: property

The expression for the receiver’s fetch request.

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
var requestExpression: NSExpression { get }
```

#### Discussion

The expression must evaluate to an [`NSFetchRequest`](nsfetchrequest.md) object.

## See Also

- [var contextExpression: NSExpression](nsfetchrequestexpression/contextexpression.md)
  The expression for the receiver’s managed object context.
- [var isCountOnlyRequest: Bool](nsfetchrequestexpression/iscountonlyrequest.md)
  Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/requestexpression)*