# model()

**Framework**: Core Animation  
**Kind**: method

Returns the model layer object associated with the receiver, if any.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func model() -> Self
```

#### Return Value

A layer instance representing the underlying model layer.

#### Discussion

Calling this method on a layer in the presentation tree returns the corresponding layer object in the model tree. This method returns a value only when a transaction involving changes to the presentation layer is in progress. If no transaction is in progress, the results of calling this method are undefined.

## See Also

- [func presentation() -> Self?](calayer/presentation.md)
  Returns a copy of the presentation layer object that represents the state of the layer as it currently appears onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/model())*