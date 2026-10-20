# name

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The name of the zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * name;
```

## See Also

### Related Documentation
- [HomeKit Developer Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
### Identifying a Zone
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the zone.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  The unique identifier for a zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmzone/name)*