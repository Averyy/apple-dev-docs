# INUIInteractiveBehavior

**Framework**: IntentsUI  
**Kind**: enum  
**Role**: Enumeration

Constants indicating how users are able to interact with your interface.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum INUIInteractiveBehavior
```

```c
enum INUIInteractiveBehavior : NSUInteger;
```

## Topics

### Enumeration Cases
- [INUIInteractiveBehavior.none](./inuiinteractivebehavior/none.md)
  No interactions
- [INUIInteractiveBehavior.nextView](./inuiinteractivebehavior/nextview.md)
  A behavior that displays controls for navigating to a new view.
- [INUIInteractiveBehavior.launch](./inuiinteractivebehavior/launch.md)
  A behavior that displays an interface to launch the app.
- [INUIInteractiveBehavior.genericAction](./inuiinteractivebehavior/genericaction.md)
  A behavior that shows an interface for performing an action.
### Initializers
- [init?(rawValue: UInt)](./inuiinteractivebehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the View Controller
- [func configureView(for: Set<INParameter>, of: INInteraction, interactiveBehavior: INUIInteractiveBehavior, context: INUIHostedViewContext, completion: (Bool, Set<INParameter>, CGSize) -> Void)](./inuihostedviewcontrolling/configureview%28for,of,interactivebehavior,context,completion%29.md)
- [func configure(with: INInteraction, context: INUIHostedViewContext, completion: (CGSize) -> Void)](./inuihostedviewcontrolling/configure%28with,context,completion%29.md)
  Configures your view controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiinteractivebehavior)*