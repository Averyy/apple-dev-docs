# setPosition(_:forDirectionPadElement:)

**Framework**: Game Controller  
**Kind**: method

Changes the value of a directional pad element in the virtual controller.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func setPosition(_ position: CGPoint, forDirectionPadElement element: String)
```

#### Discussion

Use this method to update the value of a directional pad in the virtual controller when you set the [`isHidden`](gcvirtualcontroller/configuration/ishidden.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) and present your own virtual controller interface.

## Parameters

- `position`: A point with   and   values in the range  .
- `element`: The name of the directional pad element to update.

## See Also

- [func setValue(CGFloat, forButtonElement: String)](gcvirtualcontroller/setvalue(_:forbuttonelement:).md)
  Changes the value of a button element in the virtual controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/setposition(_:fordirectionpadelement:))*