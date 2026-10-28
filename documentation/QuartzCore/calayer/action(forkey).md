# action(forKey:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Returns the action object assigned to the specified key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func action(forKey event: String) -> (any CAAction)?
```

```objc
- (id<CAAction>) actionForKey:(NSString *) event;
```

## Return Value

Returns the object that provides the action for `key`. The object must implement the [`CAAction`](../caaction.md) protocol.

## Discussion

This method searches for the given action object of the layer. Actions define dynamic behaviors for a layer. For example, the animatable properties of a layer typically have corresponding action objects to initiate the actual animations. When that property changes, the layer looks for the action object associated with the property name and executes it. You can also associate custom action objects with your layer to implement app-specific actions.

This method searches for the layer’s associated actions in the following order:

1. If the layer has a delegate that implements the [`action(for:forKey:)`](../calayerdelegate/action%28for,forkey%29.md) method, the layer calls that method. The delegate must do one of the following:

- Return the action object for the given key.
- Return the [`NSNull`](../../Foundation/nsnull.md) object if it does not handle the action.

1. The layer looks in the layer’s [`actions`](./actions.md) dictionary for a matching key/action pair.
2. The layer looks in the [`style`](./style.md) dictionary for an [`actions`](./actions.md) dictionary  for a matching key/action pair.
3. The layer calls the [`defaultAction(forKey:)`](./defaultaction%28forkey%29.md) class method to look for any class-defined actions.

If any of the above steps returns an instance of [`NSNull`](../../Foundation/nsnull.md), it is converted to `nil` before continuing.

When an action object is invoked it receives three parameters: the name of the event, the object on which the event happened (the layer), and a dictionary of named arguments specific to each event kind.

## Parameters

- `event`: The identifier of the action.

## See Also

### Related Documentation
- [Layer filters](../calayer.md#Layer-filters)
- [var style: [AnyHashable : Any]?](./style.md)
  An optional dictionary used to store property values that aren’t explicitly defined by the layer.
### Getting the layer’s actions
- [var actions: [String : any CAAction]?](./actions.md)
  A dictionary containing layer actions.
- [class func defaultAction(forKey: String) -> (any CAAction)?](./defaultaction%28forkey%29.md)
  Returns the default action for the current class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/action(forkey:))*