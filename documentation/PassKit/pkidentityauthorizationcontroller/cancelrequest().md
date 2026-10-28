# cancelRequest()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Cancels a request in progress.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func cancelRequest()
```

```objc
- (void) cancelRequest;
```

## Discussion

Use this method to cancel an in progress request. Cancellation isn’t guarenteed when you call this method, the system might return a document response if it was already in flight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityauthorizationcontroller/cancelrequest())*