# init(style:)

**Framework**: UIKit  
**Kind**: init

Creates an appearance with default values that are appropriate for the specified button style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(style: UIBarButtonItem.Style)
```

#### Return Value

A new bar button item appearance object containing the default appearances for the specified button style.

## Parameters

- `style`: The button style. UIKit uses this value to configure the default appearance attributes. For a list of possible values, see  .

## See Also

- [convenience init()](uibarbuttonitemappearance/init.md)
  Creates an appearance object with default values that are appropriate for a plain button.
- [init(coder: NSCoder)](uibarbuttonitemappearance/init(coder:).md)
  Creates an appearance object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemappearance/init(style:))*