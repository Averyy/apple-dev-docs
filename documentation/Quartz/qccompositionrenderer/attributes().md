# attributes()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the attributes of the composition associated with the renderer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func attributes() -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) attributes;
```

#### Return Value

A dictionary that contains the attributes that describe the composition, including the input and output ports of the root patch.

#### Discussion

The dictionary can define any of the attributes that are specified by the composition attribute keys. See [`QCCompositionAttributeNameKey`](../qccompositionattributenamekey.md), QCCompositionAttributeDescriptionKey, and [`QCCompositionAttributeCopyrightKey`](../qccompositionattributecopyrightkey.md).

The dictionary can also contain dictionaries that correspond to the keys that identify the input and output ports of the root patch of the composition. See QCPortAttributeTypeKey, QCPortAttributeNameKey, QCPortAttributeMinimumValueKey, QCPortAttributeMaximumValueKey, and [`QCPortAttributeMenuItemsKey`](../qcportattributemenuitemskey.md).

## See Also

### Related Documentation
- [func inputKeys() -> [Any]!](./inputkeys%28%29.md)
  Returns an array that contains the keys that identify the input ports of the root patch of the composition.
- [func outputKeys() -> [Any]!](./outputkeys%28%29.md)
  Returns an array that contains the keys that identify the output ports of the root patch of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/attributes())*