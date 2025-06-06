# SCNDetailedErrorsKey

**Framework**: SceneKit  
**Kind**: var

Detailed error information from SceneKit’s scene file loading process.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let SCNDetailedErrorsKey: String
```

#### Discussion

If SceneKit reports an error when creating or loading from a scene source, the [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary of the returned [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object may contain this key, whose value is an array of dictionaries (each containing one or more of the keys listed in [`Scene File Consistency Error Keys`](scene-file-consistency-error-keys.md)) providing details about the location of the error in the scene file.

If you specify [`true`](https://developer.apple.com/documentation/swift/true) for the [`checkConsistency`](scnscenesource/loadingoption/checkconsistency.md) option when creating or loading from a scene source, SceneKit verifies the scene file against the specification for its file format. Verifying a scene file can result in additional error reports for violations of the file format specification that do not prevent SceneKit from loading the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndetailederrorskey)*