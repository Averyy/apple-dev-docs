# default()

**Framework**: StoreKit  
**Kind**: method

Returns the default payment queue instance.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class func `default`() -> Self
```

#### Return Value

The default payment queue.

#### Discussion

Apps do not create a payment queue. Instead, they retrieve the  queue by calling this class method.

##### Special Considerations

The payment queue is not available in Simulator. Attempting to retrieve the payment queue logs a warning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/default())*