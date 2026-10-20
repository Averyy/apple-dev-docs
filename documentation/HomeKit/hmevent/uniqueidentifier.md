# uniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uniqueIdentifier: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * uniqueIdentifier;
```

## See Also

### Getting information about the event
- [class func isSupported(for: HMHome) -> Bool](./issupported%28for%29.md)
  A Boolean value indicating whether the event can be added to an event trigger on the specified home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmevent/uniqueidentifier)*