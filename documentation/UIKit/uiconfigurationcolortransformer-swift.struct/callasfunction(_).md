# callAsFunction(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Calls the transform closure of the color transformer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
func callAsFunction(_ input: UIColor) -> UIColor
```

## Discussion

Using this syntax, you can call the color transformer type as if it were a closure:

```swift
let alphaColorTransformer = UIConfigurationColorTransformer() { baseColor -> UIColor in
    return baseColor.withAlphaComponent(0.5)
}

let baseColor = UIColor.red
let modifiedColor = alphaColorTransformer(baseColor)
```

## See Also

### Calling the color transformer
- [let transform: (UIColor) -> UIColor](./transform.md)
  The transform closure of the color transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/callasfunction(_:))*