# ASIdentifierManager

**Framework**: AdSupport  
**Kind**: class  
**Role**: Class

The object that contains the advertising identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 6.0+

## Declaration

```swift
class ASIdentifierManager
```

```objc
@interface ASIdentifierManager : NSObject
```

## Topics

### Getting the Advertising Identifier
- [class func shared() -> ASIdentifierManager](./asidentifiermanager/shared%28%29.md)
  The shared instance of the identifier manager class.
- [var advertisingIdentifier: UUID](./asidentifiermanager/advertisingidentifier.md)
  The UUID that is specific to a device.
### Deprecated
- [var isAdvertisingTrackingEnabled: Bool](./asidentifiermanager/isadvertisingtrackingenabled.md)
  A Boolean value that indicates whether the user has limited ad tracking enabled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/adsupport/asidentifiermanager)*