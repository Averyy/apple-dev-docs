# numberOfLibraryItems

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An approximate number of relevant items available in the users library.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSNumber * numberOfLibraryItems;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSNumber * numberOfLibraryItems;
```

## See Also

### Accessing the Media Context Information
- [var subscriptionStatus: INMediaUserContext.SubscriptionStatus](./subscriptionstatus-swift.property.md)
  The user’s current subscription status.
- [INMediaUserContext.SubscriptionStatus](./subscriptionstatus-swift.enum.md)
  Constants that describe the current description status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediausercontext/numberoflibraryitems-881cf)*