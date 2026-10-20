# isPrimary

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this is the primary home for its home manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isPrimary: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPrimary) BOOL primary;
```

## See Also

### Identifying a home
- [var name: String](./name.md)
  The name the user gives to the home.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the home.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/isprimary)*