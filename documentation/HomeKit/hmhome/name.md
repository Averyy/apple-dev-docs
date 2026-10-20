# name

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The name the user gives to the home.

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

#### Discussion

The name should be configured by the user when a new home is created.

## See Also

### Identifying a home
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the home.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the home.
- [var isPrimary: Bool](./isprimary.md)
  A Boolean value that indicates whether this is the primary home for its home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/name)*