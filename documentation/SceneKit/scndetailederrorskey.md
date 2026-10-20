# SCNDetailedErrorsKey

**Framework**: SceneKit  
**Kind**: var  
**Role**: Global Variable

Detailed error information from SceneKit’s scene file loading process.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
let SCNDetailedErrorsKey: String
```

```c
extern NSString * const SCNDetailedErrorsKey;
```

#### Discussion

If SceneKit reports an error when creating or loading from a scene source, the [`userInfo`](../Foundation/nserror/userinfo.md) dictionary of the returned [`NSError`](../Foundation/nserror.md) object may contain this key, whose value is an array of dictionaries (each containing one or more of the keys listed in [Scene File Consistency Error Keys](./scene-file-consistency-error-keys.md)) providing details about the location of the error in the scene file.

If you specify [`true`](../Swift/true.md) for the [`checkConsistency`](./scnscenesource/loadingoption/checkconsistency.md) option when creating or loading from a scene source, SceneKit verifies the scene file against the specification for its file format. Verifying a scene file can result in additional error reports for violations of the file format specification that do not prevent SceneKit from loading the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scndetailederrorskey)*