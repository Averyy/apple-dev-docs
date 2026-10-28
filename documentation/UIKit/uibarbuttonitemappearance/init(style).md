# init(style:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an appearance with default values that are appropriate for the specified button style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(style: UIBarButtonItem.Style)
```

```objc
- (instancetype) initWithStyle:(UIBarButtonItemStyle) style;
```

## Return Value

A new bar button item appearance object containing the default appearances for the specified button style.

## Parameters

- `style`: The button style. UIKit uses this value to configure the default appearance attributes. For a list of possible values, see [`UIBarButtonItem.Style`](../uibarbuttonitem/style-swift.enum.md).

## See Also

### Creating a bar button item appearance object
- [convenience init()](./init%28%29.md)
  Creates an appearance object with default values that are appropriate for a plain button.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates an appearance object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemappearance/init(style:))*