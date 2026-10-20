# setValue(_:forButtonElement:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Changes the value of a button element in the virtual controller.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func setValue(_ value: CGFloat, forButtonElement element: String)
```

```objc
- (void) setValue:(CGFloat) value forButtonElement:(NSString *) element;
```

#### Discussion

Use this method to update the value of a button element in the virtual controller when you set the [`isHidden`](./configuration/ishidden.md) property to [`true`](../../Swift/true.md) and present your own virtual controller interface.

## Parameters

- `value`: A value in the range `[-1.0, 1.0]`.
- `element`: The name of the button element to update.

## See Also

### Presenting a custom interface
- [func setPosition(CGPoint, forDirectionPadElement: String)](./setposition%28_,fordirectionpadelement%29.md)
  Changes the value of a directional pad element in the virtual controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/setvalue(_:forbuttonelement:))*