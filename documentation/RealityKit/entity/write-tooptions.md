# write(_:to:options:)

**Framework**: RealityKit  
**Kind**: method

Exports an array of entities as separate scenes within a single RealityKit file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) static func write(_ scenes: [Entity], to url: URL, options: Entity.WriteOptions = WriteOptions()) async throws
```

#### Discussion

This method generates a file with a `.reality` suffix, automatically setting its compatibility with other systems based on all the entity tree contents. The entities and their children may contain components or assets that can require the resulting RealityKit file to be compatible with system versions between:

- iOS 18 or later
- macOS 15 or later
- visionOS 2 or later

Elements of the `entities` array must have a non-empty [`name`](entity/name.md) property. Each name must be unique within the array to allow unambiguous scene loading.

After writing, individual scenes can be loaded using the [`init(contentsOf:withName:)`](entity/init(contentsof:withname:).md) initializer with the entity’s name as the scene identifier.

Logs with the prefix [RealityKit File Compatibility Info] will be posted to the console whenever a component or asset requires a compatibility adjustment.

> **Note**: An error if any entity in the array has an empty name.

> ❗ **Important**:  During its initial setup phase, this method can indirectly block the main thread, and also has the potential to block it for the full duration of the call if the system has additional work it needs to do there.

## Parameters

- `url`: The location URL in the file system where you want to save the `.reality` file.
- `options`: Options for writing the Reality file, such as texture compression settings.

## See Also

- [func write(to: URL, options: Entity.WriteOptions) async throws](entity/write(to:options:).md)
- [Entity.WriteOptions](entity/writeoptions.md)
  A set of options that control how RealityKit writes entities to a reality file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/write(_:to:options:))*