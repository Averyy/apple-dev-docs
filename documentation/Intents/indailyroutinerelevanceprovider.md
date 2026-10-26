# INDailyRoutineRelevanceProvider

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The provider class that specifies a relevant daily routine.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INDailyRoutineRelevanceProvider
```

```objc
@interface INDailyRoutineRelevanceProvider : INRelevanceProvider
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

#### Overview

Ask the user for permission to use their location before providing shortcuts to [`INRelevantShortcutStore`](./inrelevantshortcutstore.md) that include a daily routine relevance provider. If the user gives your app permission to access their location Always, shortcuts your app provides can influence widget stacks.

## Topics

### Creating a Daily Routine Relevance Provider
- [init(situation: INDailyRoutineRelevanceProvider.Situation)](./indailyroutinerelevanceprovider/init%28situation%29.md)
  Creates a daily routine relevance provider with the specified situation.
### Getting the Situation
- [var situation: INDailyRoutineRelevanceProvider.Situation](./indailyroutinerelevanceprovider/situation-swift.property.md)
  The relevant daily routine situation for the provider.
- [INDailyRoutineRelevanceProvider.Situation](./indailyroutinerelevanceprovider/situation-swift.enum.md)
  Daily situations for a relevance provider.

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
- [class INDateRelevanceProvider](./indaterelevanceprovider.md)
  The provider class that specifies a relevant day and time.
- [class INLocationRelevanceProvider](./inlocationrelevanceprovider.md)
  The provider class that specifies a relevant location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indailyroutinerelevanceprovider)*