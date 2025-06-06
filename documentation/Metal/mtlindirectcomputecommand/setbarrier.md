# setBarrier()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Adds a barrier to ensure that commands executed prior to this command are complete before this command executes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setBarrier()
```

#### Discussion

Set or clear barriers (as needed) before encoding the command.

## See Also

- [func clearBarrier()](mtlindirectcomputecommand/clearbarrier.md)
  Removes any barrier set on the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setbarrier())*