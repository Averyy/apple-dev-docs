# PHAccessLevel

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

The app’s level of access to the user’s photo library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum PHAccessLevel
```

```c
enum PHAccessLevel : NSInteger;
```

## Topics

### Access Levels
- [PHAccessLevel.addOnly](./phaccesslevel/addonly.md)
  A value that indicates the app may only add to the user’s photo library.
- [PHAccessLevel.readWrite](./phaccesslevel/readwrite.md)
  A value that indicates the app can read from and write to the user’s photo library.
### Initializers
- [init?(rawValue: Int)](./phaccesslevel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Verifying Authorization
- [class func authorizationStatus(for: PHAccessLevel) -> PHAuthorizationStatus](./phphotolibrary/authorizationstatus%28for%29.md)
  Returns the app’s authorization to access the user’s photo library for the specified access level.
- [class func requestAuthorization(for: PHAccessLevel, handler: (PHAuthorizationStatus) -> Void)](./phphotolibrary/requestauthorization%28for,handler%29.md)
  Prompts the user to grant the app permission to access the photo library.
- [enum PHAuthorizationStatus](./phauthorizationstatus.md)
  Information about your app’s authorization to access the user’s photo library.
- [class func authorizationStatus() -> PHAuthorizationStatus](./phphotolibrary/authorizationstatus%28%29.md)
  Returns information about your app’s authorization to access the user’s photo library.
- [class func requestAuthorization((PHAuthorizationStatus) -> Void)](./phphotolibrary/requestauthorization%28_%29.md)
  Requests the user’s permission, if needed, to access the photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phaccesslevel)*