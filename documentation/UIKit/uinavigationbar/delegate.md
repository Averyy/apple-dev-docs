# delegate

**Framework**: UIKit  
**Kind**: property

The navigation bar’s delegate object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UINavigationBarDelegate)? { get set }
```

#### Discussion

The delegate must conform to the [`UINavigationBarDelegate`](uinavigationbardelegate.md) protocol. The default value is `nil`.

If the navigation bar was created by a navigation controller and is being managed by that object, you must not change the value of this property. A navigation controller acts as the delegate for the navigation bar it creates.

## See Also

- [protocol UINavigationBarDelegate](uinavigationbardelegate.md)
  Methods that a navigation bar calls before and after it modifies its stack of navigation items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/delegate)*