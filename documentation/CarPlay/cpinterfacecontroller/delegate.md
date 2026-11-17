# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A custom object you use to respond when templates appear and disappear.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var delegate: (any CPInterfaceControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<CPInterfaceControllerDelegate> delegate;
```

## Discussion

When you push and pop templates from your navigation hierarchy, you change your app’s currently visible content. The interface controller reports these changes to the custom object you assign to this property. You might use your delegate object to perform additional tasks related to the interface changes. For example, you might want to perform additional cleanup only after a template’s content isn’t visible. When defining your custom object, adopt the [`CPInterfaceControllerDelegate`](../cpinterfacecontrollerdelegate.md) protocol and use its methods to implement your changes.

## See Also

### Responding to interface changes
- [protocol CPInterfaceControllerDelegate](../cpinterfacecontrollerdelegate.md)
  The methods you implement to observe the addition and removal of templates in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/delegate)*