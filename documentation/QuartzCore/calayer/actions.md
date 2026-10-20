# actions

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A dictionary containing layer actions.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var actions: [String : any CAAction]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,id<CAAction>> * actions;
```

#### Discussion

The default value of this property is `nil`. You can use this dictionary to store custom actions for your layer. The contents of this dictionary searched as part of the standard implementation of the [`action(forKey:)`](./action%28forkey%29.md) method.

## See Also

### Getting the layer’s actions
- [func action(forKey: String) -> (any CAAction)?](./action%28forkey%29.md)
  Returns the action object assigned to the specified key.
- [class func defaultAction(forKey: String) -> (any CAAction)?](./defaultaction%28forkey%29.md)
  Returns the default action for the current class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/actions)*