# uniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the home.

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

### Identifying a home
- [var name: String](./name.md)
  The name the user gives to the home.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the home.
- [var isPrimary: Bool](./isprimary.md)
  A Boolean value that indicates whether this is the primary home for its home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/uniqueidentifier)*