# init(identifier:source:destination:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

The designated initializer for a storyboard segue.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(identifier: NSStoryboardSegue.Identifier, source sourceController: Any, destination destinationController: Any)
```

```objc
- (instancetype) initWithIdentifier:(NSStoryboardSegueIdentifier) identifier source:(id) sourceController destination:(id) destinationController;
```

## Return Value

An initialized storyboard segue, ready to be performed.

## Discussion

When a segue begins, the system calls this method. To run code during segue initialization, implement a storyboard segue subclass and override this method.

Whenever this method is called, the system then calls the [`perform()`](./perform%28%29.md) method.

## Parameters

- `identifier`: The unique identifier for the storyboard segue. See the [`identifier`](./identifier-swift.property.md) property.
- `sourceController`: The starting/containing view controller or window controller for the storyboard segue.
- `destinationController`: The ending/contained view controller or window controller for the storyboard segue.

## See Also

### Customizing Storyboard Segue Initialization and Invocation
- [convenience init(identifier: NSStoryboardSegue.Identifier, source: Any, destination: Any, performHandler: () -> Void)](./init%28identifier,source,destination,performhandler%29.md)
  Creates a storyboard segue and a block used when the segue is performed.
- [func perform()](./perform%28%29.md)
  Performs a visual transition from one controller to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue/init(identifier:source:destination:))*