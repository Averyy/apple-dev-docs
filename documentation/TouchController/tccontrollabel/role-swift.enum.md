# TCControlLabel.Role

**Framework**: Touch Controller  
**Kind**: enum  
**Role**: Enumeration

Defines the role for a control label. This determines the type of control on the touch controller’s associated GCController.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Role
```

```c
enum TCControlLabelRole : NSInteger;
```

## Topics

### Roles
- [TCControlLabel.Role.button](./role-swift.enum/button.md)
  A label for a button input controller.
- [TCControlLabel.Role.directionPad](./role-swift.enum/directionpad.md)
  A label for a direction pad controller.
### Creating a role
- [init?(rawValue: Int)](./role-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the control
- [var role: TCControlLabel.Role](./role-swift.property.md)
  The type of the control label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrollabel/role-swift.enum)*