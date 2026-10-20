# UINavigationController.Operation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define the type of navigation controller transitions that can occur.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Operation
```

```c
enum UINavigationControllerOperation : NSInteger;
```

## Topics

### Constants
- [UINavigationController.Operation.none](./operation/none.md)
  A constant that indicates no operation is taking place.
- [UINavigationController.Operation.push](./operation/push.md)
  A constant that indicates a view controller is being pushed onto the navigation stack.
- [UINavigationController.Operation.pop](./operation/pop.md)
  A constant that indicates the topmost view controller is being removed from the navigation stack.
### Initializers
- [init?(rawValue: Int)](./operation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/operation)*