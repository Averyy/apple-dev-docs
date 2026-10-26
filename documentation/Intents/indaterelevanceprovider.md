# INDateRelevanceProvider

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The provider class that specifies a relevant day and time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INDateRelevanceProvider
```

```objc
@interface INDateRelevanceProvider : INRelevanceProvider
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

## Topics

### Creating a Date Relevance Provider
- [init(start: Date, end: Date?)](./indaterelevanceprovider/init%28start,end%29.md)
  Creates a relevance provider with the specified start and end dates.
### Getting the Relevant Dates
- [var startDate: Date](./indaterelevanceprovider/startdate.md)
  The relevant start date.
- [var endDate: Date?](./indaterelevanceprovider/enddate.md)
  The relevant end date.
### Initializers
- [init(startDate: Date, endDate: Date?)](./indaterelevanceprovider/init%28startdate,enddate%29.md)

## Relationships

### Inherits From
- [INRelevanceProvider](./inrelevanceprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Relevance Providers
- [class INRelevanceProvider](./inrelevanceprovider.md)
  An abstract class that represents a relevance provider.
- [class INDailyRoutineRelevanceProvider](./indailyroutinerelevanceprovider.md)
  The provider class that specifies a relevant daily routine.
- [class INLocationRelevanceProvider](./inlocationrelevanceprovider.md)
  The provider class that specifies a relevant location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indaterelevanceprovider)*