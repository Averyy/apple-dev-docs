# PKAddPassesViewControllerDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol  
**Role**: Protocol

Methods that an add-passes view controller’s delegate implements.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
protocol PKAddPassesViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol PKAddPassesViewControllerDelegate <NSObject>
```

## Topics

### Delegate methods
- [func addPassesViewControllerDidFinish(PKAddPassesViewController)](./pkaddpassesviewcontrollerdelegate/addpassesviewcontrollerdidfinish%28_%29.md)
  Sent to the delegate after the add-passes view controller has finished.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Adding passes
- [var delegate: (any PKAddPassesViewControllerDelegate)?](./pkaddpassesviewcontroller/delegate.md)
  The view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontrollerdelegate)*