# defaultAction(forKey:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

Returns the default action for the current class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func defaultAction(forKey event: String) -> (any CAAction)?
```

```objc
+ (id<CAAction>) defaultActionForKey:(NSString *) event;
```

## Return Value

Returns a suitable action object for the given key or `nil` of no action object was associated with that key.

## Discussion

Classes that want to provide default actions can override this method and use it to return those actions.

## Parameters

- `event`: The identifier of the action.

## See Also

### Getting the layer’s actions
- [func action(forKey: String) -> (any CAAction)?](./action%28forkey%29.md)
  Returns the action object assigned to the specified key.
- [var actions: [String : any CAAction]?](./actions.md)
  A dictionary containing layer actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/defaultaction(forkey:))*