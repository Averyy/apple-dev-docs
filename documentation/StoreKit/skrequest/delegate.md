# delegate

**Framework**: StoreKit  
**Kind**: property

The delegate of the request object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
weak var delegate: (any SKRequestDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`SKRequestDelegate`](skrequestdelegate.md) protocol, although most subclasses of [`SKRequest`](skrequest.md) provide a more specific protocol to implement.

## See Also

- [protocol SKRequestDelegate](skrequestdelegate.md)
  Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequest/delegate)*