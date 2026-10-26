# INLocationRelevanceProvider

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The provider class that specifies a relevant location.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- watchOS 5.0+

## Declaration

```swift
class INLocationRelevanceProvider
```

```objc
@interface INLocationRelevanceProvider : INRelevanceProvider
```

#### Overview

Ask the user for permission to use their location before providing shortcuts to [`INRelevantShortcutStore`](./inrelevantshortcutstore.md) that include a location relevance provider. If the user gives your app permission to access their location While In Use or Always_,_ shortcuts your app provides can influence widget stacks and the Siri watch face.

## Topics

### Creating a Location Relevance Provider
- [init(region: CLRegion)](./inlocationrelevanceprovider/init%28region%29.md)
  Creates a relevance provider for a location specified as a region.
### Getting the Relevant Region
- [var region: CLRegion](./inlocationrelevanceprovider/region.md)
  The region representing the relevant location.

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
- [class INDateRelevanceProvider](./indaterelevanceprovider.md)
  The provider class that specifies a relevant day and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlocationrelevanceprovider)*