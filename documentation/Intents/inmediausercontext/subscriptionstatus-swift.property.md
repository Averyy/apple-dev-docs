# subscriptionStatus

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s current subscription status.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var subscriptionStatus: INMediaUserContext.SubscriptionStatus { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) INMediaUserContextSubscriptionStatus subscriptionStatus;
```

*macOS*

```objc
@property (atomic, assign, readwrite) INMediaUserContextSubscriptionStatus subscriptionStatus;
```

## See Also

### Accessing the Media Context Information
- [var numberOfLibraryItems: Int?](./numberoflibraryitems-8rnf0.md)
  An approximate number of relevant items available in the users library.
- [INMediaUserContext.SubscriptionStatus](./subscriptionstatus-swift.enum.md)
  Constants that describe the current description status.
- [numberOfLibraryItems](./numberoflibraryitems-881cf.md)
  An approximate number of relevant items available in the users library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediausercontext/subscriptionstatus-swift.property)*