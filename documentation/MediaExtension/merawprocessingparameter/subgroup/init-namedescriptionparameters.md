# init(name:description:parameters:)

**Framework**: MediaExtension  
**Kind**: init

Creates a sub group parameter object with the parameters value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(name: String, description: String, parameters: [MERAWProcessingParameter])
```

#### Return Value

An instance of [`MERAWProcessingParameter.SubGroup`](merawprocessingparameter/subgroup.md).

## Parameters

- `name`: A localized human-readable name for the parameter, suitable for displaying in application UI.
- `description`: A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- `parameters`: The array of   objects in the sub group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/subgroup/init(name:description:parameters:))*