# setVisibilityResultMode(_:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures a visibility test for Metal to run, and the destination for any results it generates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset: Int)
```

#### Discussion

You use the `mode` parameter to enable or disable the visibility test, and determine if it produces a boolean response for passing fragments, or if it counts the number of fragments.

## Parameters

- `mode`: A [`MTLVisibilityResultMode`](mtlvisibilityresultmode.md) that configures which visibility test results the render pass saves to a buffer, or disables visibility testing.
- `offset`: A location, in bytes, relative to the start of [`visibilityResultBuffer`](mtl4renderpassdescriptor/visibilityresultbuffer.md) The GPU stores the result of a visibility test at `offset`, which needs to be a multiple of `8`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setvisibilityresultmode(_:offset:))*