# delegate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the request object.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: No longer supported.

## Declaration

```swift
weak var delegate: (any SKRequestDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<SKRequestDelegate> delegate;
```

## Discussion

The delegate must adopt the [`SKRequestDelegate`](../skrequestdelegate.md) protocol, although most subclasses of [`SKRequest`](../skrequest.md) provide a more specific protocol to implement.

## See Also

### Accessing the Delegate
- [protocol SKRequestDelegate](../skrequestdelegate.md)
  Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequest/delegate)*