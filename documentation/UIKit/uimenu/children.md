# children

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The contents of the menu.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var children: [UIMenuElement] { get }
```

```objc
@property (nonatomic, readonly) NSArray<UIMenuElement *> * children;
```

## Discussion

If the menu doesn’t have any child menu elements, this property contains an empty array.

## See Also

### Accessing child elements
- [func replacingChildren([UIMenuElement]) -> UIMenu](./replacingchildren%28_%29.md)
  Creates a new menu with the same configuration as the current menu, but with a new set of child elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenu/children)*