# setArgumentTable(_:stages:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Associates an argument table with a set of render stages.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setArgumentTable(_ argumentTable: any MTL4ArgumentTable, stages: MTLRenderStages)
```

#### Discussion

Metal takes a snapshot of the resources in the argument table when you encode a draw, dispatch, or execute command. This snapshot becomes available to the `stages` you specify to this method.

## Parameters

- `argumentTable`:   to set.
- `stages`: A   bitmask that specifies the shader stages with visibility over the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setargumenttable(_:stages:))*