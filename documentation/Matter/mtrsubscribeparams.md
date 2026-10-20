# MTRSubscribeParams

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRSubscribeParams
```

```objc
@interface MTRSubscribeParams : MTRReadParams
```

## Topics

### Initializers
- [init(minInterval: NSNumber, maxInterval: NSNumber)](./mtrsubscribeparams/init%28mininterval,maxinterval%29.md)
### Instance Properties
- [var autoResubscribe: NSNumber?](./mtrsubscribeparams/autoresubscribe.md)
- [var keepPreviousSubscriptions: NSNumber?](./mtrsubscribeparams/keepprevioussubscriptions.md)
- [var maxInterval: NSNumber](./mtrsubscribeparams/maxinterval.md)
- [var minInterval: NSNumber](./mtrsubscribeparams/mininterval.md)
- [var shouldReplaceExistingSubscriptions: Bool](./mtrsubscribeparams/shouldreplaceexistingsubscriptions.md)
- [var shouldReportEventsUrgently: Bool](./mtrsubscribeparams/shouldreporteventsurgently.md)
- [var shouldResubscribeAutomatically: Bool](./mtrsubscribeparams/shouldresubscribeautomatically.md)
### Type Methods
- [class func new() -> Self](./mtrsubscribeparams/new%28%29.md)

## Relationships

### Inherits From
- [MTRReadParams](./mtrreadparams.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrsubscribeparams)*