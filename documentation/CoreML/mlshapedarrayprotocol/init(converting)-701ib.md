# init(converting:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array type by converting another shaped array type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init<T>(converting source: T) where T : MLShapedArrayProtocol
```

**Other overloads**:

```swift
init(converting multiArray: MLMultiArray)
```

## Parameters

- `source`: An instance with a type that conforms to [`MLShapedArrayProtocol`](../mlshapedarrayprotocol.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/init(converting:)-701ib)*