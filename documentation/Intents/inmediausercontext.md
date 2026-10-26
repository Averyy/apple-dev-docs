# INMediaUserContext

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that provides user information to Siri.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INMediaUserContext
```

```objc
@interface INMediaUserContext : INUserContext
```

## Mentions

- [Improving Siri Media Interactions and App Selection](../SiriKit/improving-siri-media-interactions-and-app-selection.md)

#### Overview

When your media app launches, create an [`INMediaUserContext`](./inmediausercontext.md). Provide the number of items the user has in their library and indicate whether the user has a current paid subscription. Then call [`becomeCurrent()`](./inusercontext/becomecurrent%28%29.md) to share this user context with the system. The following code listing shows how to set the current context for a user with a paid subscription and a few hundred items in their library:

```swift
let context = INMediaUserContext()
context.numberOfLibraryItems = 345
context.subscriptionStatus = .subscribed
context.becomeCurrent()
```

## Topics

### Creating a new Media User Context
- [init()](./inmediausercontext/init%28%29.md)
  Creates a new media user context object.
### Accessing the Media Context Information
- [var numberOfLibraryItems: Int?](./inmediausercontext/numberoflibraryitems-8rnf0.md)
  An approximate number of relevant items available in the users library.
- [var subscriptionStatus: INMediaUserContext.SubscriptionStatus](./inmediausercontext/subscriptionstatus-swift.property.md)
  The user’s current subscription status.
- [INMediaUserContext.SubscriptionStatus](./inmediausercontext/subscriptionstatus-swift.enum.md)
  Constants that describe the current description status.

## Relationships

### Inherits From
- [INUserContext](./inusercontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### User Context
- [class INUserContext](./inusercontext.md)
  An object that provides user information to Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediausercontext)*