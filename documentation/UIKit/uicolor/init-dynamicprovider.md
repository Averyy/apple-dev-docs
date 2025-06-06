# init(dynamicProvider:)

**Framework**: UIKit  
**Kind**: init

Creates a color object that uses the specified block to generate its color data dynamically.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(dynamicProvider: @escaping (UITraitCollection) -> UIColor)
```

#### Return Value

A color object whose color information is provided by the specified block.

#### Discussion

Use this method to create a color object whose component values change based on the currently active traits. The block you provide creates a new color object based on the traits in the provided trait collection.

## Parameters

- `dynamicProvider`: A block that determines the appropriate color values based on the specified traits. This block returns a   object and takes a single parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(dynamicprovider:))*