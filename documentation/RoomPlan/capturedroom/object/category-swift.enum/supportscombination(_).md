# supportsCombination(_:)

**Framework**: RoomPlan  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a category supports the given attribute combination.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func supportsCombination(_ attributes: [any CapturedRoomAttribute]) -> Bool
```

## Discussion

Only compatible attributes can pair up in association with a 3D model, for example, with the [`CapturedRoom.ModelProvider`](../../modelprovider.md) function [`setModelFileURL(_:for:)`](../../modelprovider/setmodelfileurl%28_,for%29-8xio.md). These [`CapturedRoom.ModelProvider`](../../modelprovider.md) functions for `setModelFileURL` and `modelFileURL` throw [`CapturedRoom.ModelProvider.Error.attributeCombinationNotSupported`](../../modelprovider/error/attributecombinationnotsupported.md) if no object category supports all of the attributes in the arguments to their call.

## Parameters

- `attributes`: An array of attributes to check whether the object supports them.

## See Also

### Determining supported attributes
- [var supportedAttributeTypes: [any CapturedRoomAttribute.Type]](./supportedattributetypes.md)
  Defines the attributes types compatible with a particular object category.
- [var supportedCombinations: [[any CapturedRoomAttribute]]](./supportedcombinations.md)
  An array of supported attributes that differs by category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/object/category-swift.enum/supportscombination(_:))*