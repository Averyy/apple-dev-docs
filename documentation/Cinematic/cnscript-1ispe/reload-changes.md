# reload(changes:)

**Framework**: Cinematic  
**Kind**: method

Reloads the Cinematic script with optional changes applied, removing any previous changes made.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func reload(changes: CNScript.Changes?)
```

#### Discussion

Reloading the Cinematic script can be more efficient than loading the asset from scratch.

You can obtain the applied changes from a previous editing session. The system reloads the asset as originally recoded if the changes value is nil.

## Parameters

- `changes`: Optional changes since recording the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/reload(changes:))*