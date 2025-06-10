# setVisibilityResultMode(_:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures a visibility test for Metal to run, and the destination for any results it generates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset: Int)
```

#### Discussion

You use the `mode` parameter to enable or disable the visibility test, and determine if it produces a boolean response for passing fragments, or if it counts the number of fragments.

## Parameters

- `mode`: A   that configures which visibility test results   the render pass saves to a buffer, or disables visibility testing.
- `offset`: A location, in bytes, relative to the start of    The GPU stores   the result of a visibility test at  , which needs to be a multiple of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setvisibilityresultmode(_:offset:))*