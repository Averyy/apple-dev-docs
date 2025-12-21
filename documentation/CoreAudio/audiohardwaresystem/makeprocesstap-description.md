# makeProcessTap(description:)

**Framework**: Core Audio  
**Kind**: method

Creates a new tap using the provided description.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func makeProcessTap(description: CATapDescription) throws -> AudioHardwareTap?
```

#### Return Value

An AudioHardwareTap representing the newly created tap.

## Parameters

- `description`: The CATapDescription that specifies how to build the Tap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem/makeprocesstap(description:))*