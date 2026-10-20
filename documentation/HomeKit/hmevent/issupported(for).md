# isSupported(for:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Type Method

A Boolean value indicating whether the event can be added to an event trigger on the specified home.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func isSupported(for home: HMHome) -> Bool
```

```objc
+ (BOOL) isSupportedForHome:(HMHome *) home;
```

## See Also

### Getting information about the event
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmevent/issupported(for:))*