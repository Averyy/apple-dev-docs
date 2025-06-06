# changeToMode(with:completion:)

**Framework**: Matter  
**Kind**: method

Command ChangeToMode

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func changeToMode(with params: MTRDishwasherModeClusterChangeToModeParams) async throws -> MTRDishwasherModeClusterChangeToModeResponseParams
```

#### Discussion

This command is used to change device modes. On receipt of this command the device SHALL respond with a ChangeToModeResponse command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdishwashermode/changetomode(with:completion:))*