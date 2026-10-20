# uniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for a zone.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
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

### Identifying a Zone
- [var name: String](./name.md)
  The name of the zone.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/uniqueidentifier)*