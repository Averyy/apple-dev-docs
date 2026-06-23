# isAvailable(on:version:)

**Framework**: RealityKit  
**Kind**: method

Returns whether this node definition is available on a given platform and OS version.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func isAvailable(on platform: ShaderGraph.NodeDefinition.Platform, version: OperatingSystemVersion? = nil) -> Bool
```

#### Return Value

`true` if this definition is available on `platform` at `version`; `false` if it is unavailable or has been obsoleted by that version.

#### Discussion

Use this method to filter node definitions before presenting them to the user, or before adding them to a graph that targets a specific deployment target.

```swift
let library = ShaderGraph.NodeLibrary(version: .materialX138)
let currentVersion = ProcessInfo.processInfo.operatingSystemVersion

let supportedDefinitions = library.definitions.filter {
    $0.isAvailable(on: .iOS, version: currentVersion)
}
```

## Parameters

- `platform`: The platform to check availability for.
- `version`: The OS version to check against. When `nil`, returns `true` if the definition is available on the platform at any version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/isavailable(on:version:))*