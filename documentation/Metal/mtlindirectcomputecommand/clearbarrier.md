# clearBarrier()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Removes any barrier set on the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func clearBarrier()
```

#### Discussion

You must set or clear barriers (as needed) before executing any of the commands in the indirect command buffer.

## See Also

- [func setBarrier()](mtlindirectcomputecommand/setbarrier.md)
  Adds a barrier to ensure that commands executed prior to this command are complete before this command executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/clearbarrier())*