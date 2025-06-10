# setVertexAmplificationCount(_:)

**Framework**: Metal  
**Kind**: method

Sets the vertex amplification count and its view mapping for each amplification ID.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setVertexAmplificationCount(_ viewMappings: [MTLVertexAmplificationViewMapping])
```

#### Discussion

Each view mapping element describes how to route the corresponding amplification ID to a specific viewport and render target array index by using offsets from the base array index provided by the `[[ render_target_array_index ]]` and/or `[[ viewport_array_index ]]` output attributes in the vertex shader. This allows Metal to route each amplified vertex to a different `[[ render_target_array_index ]]` and `[[ viewport_array_index ]]`, even though you can’t directly amplify these attributes.

## Parameters

- `viewMappings`: A Swift array of   elements. Each element in the array provides   per-output offsets to a specific render target and viewport


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setvertexamplificationcount(_:)-911ja)*