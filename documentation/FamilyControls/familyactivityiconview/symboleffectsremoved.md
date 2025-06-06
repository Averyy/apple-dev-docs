# symbolEffectsRemoved(_:)

**Framework**: FamilyControls  
**Kind**: method

Returns a new view with its inherited symbol image effects either removed or left unchanged.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func symbolEffectsRemoved(_ isEnabled: Bool = true) -> some View
```

#### Return Value

A copy of the view with its symbol effects either removed or left unchanged.

#### Discussion

The following example adds a repeating pulse effect to two symbol images, but then disables the effect on one of them:

```swift
VStack {
    Image(systemName: "bolt.slash.fill") // does not pulse
        .symbolEffectsRemoved()
    Image(systemName: "folder.fill.badge.person.crop") // pulses
}
.symbolEffect(.pulse)
```

## Parameters

- `isEnabled`: Whether to remove inherited symbol   effects or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/symboleffectsremoved(_:))*