# presentation()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Returns a copy of the presentation layer object that represents the state of the layer as it currently appears onscreen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func presentation() -> Self?
```

```objc
- (instancetype) presentationLayer;
```

#### Return Value

A copy of the current presentation layer object.

#### Discussion

The layer object returned by this method provides a close approximation of the layer that is currently being displayed onscreen. While an animation is in progress, you can retrieve this object and use it to get the current values for those animations.

The [`sublayers`](./sublayers.md), [`mask`](./mask.md), and [`superlayer`](./superlayer.md) properties of the returned layer return the corresponding objects from the presentation tree (not the model tree). This pattern also applies to any read-only layer methods. For example, the [`hitTest(_:)`](./hittest%28_%29.md) method of the returned object queries the layer objects in the presentation tree.

## See Also

### Accessing related layer objects
- [func model() -> Self](./model%28%29.md)
  Returns the model layer object associated with the receiver, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/presentation())*